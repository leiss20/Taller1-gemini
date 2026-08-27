import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar las variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)
# Verificar que exista la API Key
if not API_KEY:
    raise ValueError("No se encontró la variable GENAI_API_KEY en el archivo .env")

# Inicializar el cliente de Gemini
client = genai.Client(api_key=API_KEY)

# Configuración del modelo
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""
    Eres un asistente especializado en Inteligencia Artificial.
    Explica los conceptos de forma clara, concisa y educativa.
    """
)

# Consulta
text = """
Explica qué es la "Inferencia en IA".
La explicación debe tener menos de 50 palabras.
"""

# Realizar la petición a Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    config=configuration,
    contents=text
)

# Mostrar la respuesta
print("\nRespuesta de Gemini:")
print(response.text)
