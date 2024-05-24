# Proyecto de ChatBot con RAG y FastAPI

Bienvenido a esta guía paso a paso para inicializar un proyecto con FastAPI. Este documento te ayudará a configurar tu entorno, instalar las dependencias necesarias y ejecutar tu proyecto con FastAPI utilizando un archivo `requirements.txt`.

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Editor de código (recomendado: VS Code)

## Configuración del Entorno

Es una buena práctica crear un entorno virtual para tu proyecto. Esto te permite gestionar las dependencias de tu proyecto de manera aislada. Para crear y activar un entorno virtual, sigue estos pasos:

```bash
# Crear un entorno virtual
python -m venv nombre_entorno_virtual

# Activar el entorno virtual en Windows
.\nombre_entorno_virtual\Scripts\activate

# Activar el entorno virtual en macOS/Linux
source nombre_entorno_virtual/bin/activate

# Cargar dependencias
pip install -r requirements.txt
```

## Inicializar proyecto
Comenzar a utilizar el proyecto y utilizar la aplicación por completo.

Crear archivo .env con las variables:
```bash
EMBEDDING_MODEL_NAME = 'embedding-model'
DOCUMENT_PATH='path-file.txt'
MODEL_NAME = 'model-name'
```
Ejecutar comando: 
```bash
uvicorn src.main:app --reload
```

## Probar aplicación

Puedes probar desde la documentación generada por FastAPI ingresando a la URL: http://127.0.0.1:8000/docs o http://localhost:8000/docs.

El endpoint a probar es /question, así que la ruta para ejecutar es la siguiente:

http://localhost:8000/question

Cuerpo necesario para llamar el endpoint:
```bash
{
	"question": "pregunta sobre el archivo"
}
```