import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables del archivo .env
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró la variable GENAI_API_KEY en el archivo .env")

# Inicializar el cliente de Gemini
client = genai.Client(api_key=API_KEY)


def procesar_articulo(texto, tarea):
    """
    Procesa un artículo según la tarea indicada:
    - resumir: genera un resumen ejecutivo.
    - profesionalizar: convierte el texto a un estilo formal y técnico.
    """

    # System instruction obligatoria del ejercicio
    configuration = types.GenerateContentConfig(
        max_output_tokens=2048,
        system_instruction="""
        Eres un "Editor Editorial de prestigio".

        Tu función es procesar textos con un alto nivel de calidad,
        precisión, claridad y corrección profesional.

        Si la tarea es resumir, genera un resumen ejecutivo
        que conserve las ideas principales del texto.

        Si la tarea es profesionalizar, transforma el texto
        para que tenga un lenguaje formal y técnico,
        manteniendo el significado original.
        """,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )

    # Determinar la tarea
    if tarea.lower() == "resumir":
        instruccion = f"""
        Realiza un resumen ejecutivo del siguiente artículo.
        Identifica las ideas principales y presenta la información
        de forma clara y concisa.

        ARTÍCULO:
        {texto}
        """

    elif tarea.lower() == "profesionalizar":
        instruccion = f"""
        Profesionaliza el siguiente artículo.
        Utiliza un lenguaje formal, técnico y profesional.
        Conserva las ideas y el significado original, pero mejora
        la redacción, precisión y estructura.

        ARTÍCULO:
        {texto}
        """

    else:
        return "Error: la tarea debe ser 'resumir' o 'profesionalizar'."

    # Enviar la solicitud a Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        config=configuration,
        contents=instruccion
    )

    return response.text


# Ejemplo de uso
articulo = """
La inteligencia artificial está cambiando muchas industrias.
Las empresas utilizan modelos de IA para analizar grandes cantidades
de información, automatizar procesos y mejorar la toma de decisiones.
Sin embargo, también existen desafíos relacionados con la seguridad,
la privacidad y el uso responsable de estas tecnologías.
"""

print("=== RESUMEN EJECUTIVO ===")
print(procesar_articulo(articulo, "resumir"))

print("\n=== TEXTO PROFESIONALIZADO ===")
print(procesar_articulo(articulo, "profesionalizar"))
