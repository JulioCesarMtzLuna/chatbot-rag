from transformers import RagTokenizer, RagSequenceForGeneration, RagRetriever
import os
from dotenv import load_dotenv

load_dotenv()

class Generator:
    def __init__(self, dataset):
        model_name = os.getenv("MODEL_NAME")
        self.tokenizer = RagTokenizer.from_pretrained(model_name)

        faiss_document_url = os.path.join(os.path.dirname(__file__), 'data', 'faiss_index.index')
        self.retriever = RagRetriever.from_pretrained(
            model_name,
            index_name="legacy",
            passages_path=faiss_document_url,
            indexed_dataset=dataset,
        )
        self.model = RagSequenceForGeneration.from_pretrained(model_name, retriever=self.retriever)
        
        
    async def generate_answer(self, context, question):
        retriever_inputs = self.tokenizer(
            question, 
            context, 
            return_tensors="pt", 

        )
        retriever_results = self.retriever(
            question_input_ids=retriever_inputs["input_ids"],
            question_hidden_states=retriever_inputs["attention_mask"],
        )
        passage_ids = retriever_results["passage_ids"]
        inputs = self.tokenizer(
            question,
            context,
            return_tensors="pt",
            padding="max_length",
            truncation="only_second",
            max_length=100
        )
        generated_ids = self.model(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            context_input_ids=passage_ids,
            max_length=100,
            num_return_sequences=1,
            early_stopping=True
        )
        generated_answer = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        
        return generated_answer[0]
    