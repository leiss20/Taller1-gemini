import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    raise ValueError(
        "No se encontró la variable GENAI_API_KEY en el archivo .env"
    )


# Inicializar el cliente
client = genai.Client(api_key=API_KEY)


# Configuración del vendedor
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    temperature=0,
    system_instruction="""
Eres un vendedor amable, profesional y experto de una tienda
de tecnología.

Tu función es ayudar a los clientes con preguntas sobre TODO tipo
de productos tecnológicos, sin limitarte a una marca o catálogo
específico.

Puedes responder preguntas sobre:

- Computadores y portátiles
- Celulares y tablets
- Monitores
- Teclados
- Mouse
- Audífonos y auriculares
- Parlantes
- Cámaras
- Impresoras
- Componentes de PC
- Tarjetas gráficas
- Procesadores
- Memoria RAM
- Discos SSD y HDD
- Accesorios y periféricos
- Consolas y videojuegos
- Smartwatches
- Otros dispositivos tecnológicos

Puedes hablar sobre cualquier marca, por ejemplo:

HP, Acer, ASUS, Lenovo, Dell, Apple, Samsung, Logitech,
Razer, Sony, Corsair, Xiaomi, JBL, Microsoft y otras.

REGLAS:

1. Responde de forma amable, clara y profesional.

2. Cuando el usuario pregunte por un producto, proporciona
   sus características y especificaciones técnicas cuando
   tengas información suficiente.

3. Si el usuario menciona solamente una familia o línea de
   productos, como "Acer Aspire", explica las características
   generales de esa familia y pregunta si desea un modelo específico.

4. Si el usuario pregunta por "el más reciente", "el último modelo"
   o información que dependa de datos actuales, no inventes la
   respuesta. Indica que necesitas el modelo exacto o información
   actualizada para confirmar las especificaciones.

5. Si el usuario pregunta por un producto que no conoces
   suficientemente, dilo claramente en lugar de inventar datos.

6. Si el usuario pregunta por un producto tecnológico diferente
   a los ejemplos del historial, responde normalmente.

7. Utiliza el historial Few-Shot como ejemplo del estilo de respuesta,
   pero NO limites tus respuestas únicamente a los productos
   mencionados en el historial.

8. Mantén el contexto de la conversación.
"""
)


# ============================================================
# HISTORIAL FEW-SHOT
# ============================================================

history = [

    # -------- EJEMPLO 1 --------

    types.Content(
        role="user",
        parts=[
            types.Part.from_text(
                text="¿Qué especificaciones tiene el portátil HP?"
            )
        ]
    ),

    types.Content(
        role="model",
        parts=[
            types.Part.from_text(
                text="""
HP tiene diferentes líneas de portátiles, como Aspire, Pavilion,
Envy, OmniBook, ProBook y EliteBook. Las especificaciones dependen
del modelo específico. Si me indicas el modelo exacto, puedo
ayudarte con procesador, memoria RAM, almacenamiento, pantalla
y otras características.
"""
            )
        ]
    ),


    # -------- EJEMPLO 2 --------

    types.Content(
        role="user",
        parts=[
            types.Part.from_text(
                text="¿Qué especificaciones tiene un mouse Logitech?"
            )
        ]
    ),

    types.Content(
        role="model",
        parts=[
            types.Part.from_text(
                text="""
Logitech cuenta con diferentes modelos de mouse para oficina,
productividad y gaming. Las características pueden incluir
sensor óptico, conexión inalámbrica o cableada, botones
programables, diferentes niveles de DPI y batería recargable
en algunos modelos. Si me indicas el modelo exacto, puedo
darte sus especificaciones concretas.
"""
            )
        ]
    )
]


# ============================================================
# CREAR CHAT
# ============================================================

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=configuration,
    history=history
)


# ============================================================
# INTERFAZ DEL CHAT
# ============================================================

print("----------------------------------------------")
print("   CHAT DE SOPORTE - TIENDA DE TECNOLOGÍA")
print("----------------------------------------------")
print("Hola, soy tu vendedor virtual.")
print("Puedes preguntarme sobre cualquier producto")
print("o marca de tecnología.")
print("")
print("Escribe 'finalizar' para terminar.")
print("----------------------------------------------\n")


# ============================================================
# BUCLE PRINCIPAL
# ============================================================

while True:

    user_input = input("Cliente: ")

    if user_input.lower().strip() in [
        "finalizar",
        "salir",
        "exit",
        "quit"
    ]:
        print("\nVendedor: ¡Gracias por visitar nuestra tienda!")
        print("¡Hasta pronto!")
        break

    if not user_input.strip():
        print("Vendedor: Por favor, escribe una pregunta.")
        continue

    try:

        response = chat.send_message(user_input)

        # Obtener el texto de la respuesta
        respuesta = response.text

        if respuesta:
            print(f"\nVendedor: {respuesta}\n")
        else:
            print("\nVendedor: No pude generar una respuesta.\n")

    except Exception as e:

        print(f"\nError al procesar la solicitud: {e}\n")
