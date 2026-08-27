# 🤖 Taller 1 - Inteligencia Artificial con Google Gemini

<div align="center">

### Desarrollo de ejercicios utilizando la API de Google Gemini

**Asignatura:** Inteligencia Artificial  
**Año:** 2026  
**Repositorio:** [Taller1-gemini](https://github.com/leiss20/Taller1-gemini)

</div>

---

## 📋 Descripción

Este repositorio contiene el desarrollo del **Taller 1 de Inteligencia Artificial**, cuyo objetivo es implementar diferentes funcionalidades utilizando la API de **Google Gemini** mediante Python.

Durante el desarrollo del taller se implementaron tres ejercicios:

| Ejercicio | Descripción |
|-----------|-------------|
| 🧠 **Ejercicio 1** | Conexión y petición básica a Gemini |
| 📝 **Ejercicio 2** | Procesador inteligente de textos |
| 💬 **Ejercicio 3** | Chat de soporte con historial y Few-Shot |

---

# 🛠️ Tecnologías utilizadas

- 🐍 **Python 3.12**
- 🤖 **Google Gemini API**
- 📦 **Google GenAI SDK**
- 🔐 **python-dotenv**
- 🌐 **Requests**
- 💻 **Visual Studio Code**
- 🔧 **Git / GitHub**

---

# 📁 Estructura del proyecto

```text
Taller1-gemini/
│
├── 📄 ejercicio1.py
├── 📄 ejercicio2.py
├── 📄 ejercicio3.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
│
├── 📂 evidencias/
│   ├── 🖼️ ejercicio1.png
│   ├── 🖼️ ejercicio2.png
│   └── 🖼️ ejercicio3.png
│
└── 🔒 .env

⚙️ Requisitos previos
Antes de ejecutar los ejercicios se necesita tener instalado:

Python 3.12 o superior compatible.
Visual Studio Code.
Conexión a Internet.
Una API Key de Google Gemini.



🚀 Instalación
1. Clonar el repositorio
Desde la terminal de Visual Studio Code:

git clone https://github.com/leiss20/Taller1-gemini.git

2.Crear un entorno virtual
Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

En Windows:

python -m venv venv

3.Crear un entorno virtual
Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

En Windows:

python -m venv venv

4. Instalar las dependencias
Con el entorno virtual activado, ejecute:

python -m pip install -r requirements.txt

🔑 Configuración de la API Key
Para ejecutar los ejercicios es necesario configurar una API Key de Google Gemini.

1. Crear el archivo .env
En la carpeta principal del proyecto cree un archivo llamado:

.env

Dentro del archivo agregue:

GENAI_API_KEY=TU_API_KEY_AQUI

Reemplace TU_API_KEY_AQUI por su propia API Key.

▶️ Ejercicio 1 - Conexión y petición básica
Descripción
Este ejercicio inicializa el cliente de Google Gemini y realiza una consulta básica.

La IA recibe la instrucción de explicar qué es la Inferencia en IA utilizando menos de 50 palabras.

Ejecución
Con el entorno virtual activado, ejecute:

python ejercicio1.py

El programa realizará una consulta a Gemini y mostrará la respuesta generada en la terminal.

Ejemplo de salida
La inferencia en IA es el proceso mediante el cual un modelo
utiliza los conocimientos aprendidos durante su entrenamiento
para analizar nuevos datos y generar una predicción, clasificación
o respuesta.

📸 Evidencia - Ejercicio 1
<img width="1253" height="153" alt="image" src="https://github.com/user-attachments/assets/d6d6283a-0571-4915-b87f-549512ecf853" />

▶️ Ejercicio 2 - Procesador de textos inteligente
Descripción
Este ejercicio implementa una función llamada:

procesar_articulo(texto, tarea)

La función recibe un texto y una tarea.

Se pueden realizar dos operaciones:

📝 Resumir
Cuando la tarea es:

resumir

Gemini genera un resumen ejecutivo del texto proporcionado.

✍️ Profesionalizar
Cuando la tarea es:

profesionalizar

Gemini modifica el texto para utilizar un lenguaje más formal, técnico y profesional.

Además, se utiliza una system_instruction que define a la IA como un:

"Editor Editorial de prestigio"

Ejecución
Ejecute:

python ejercicio2.py

El programa mostrará los resultados correspondientes al resumen y a la profesionalización del artículo.

Ejemplo de salida
=== RESUMEN EJECUTIVO ===

[Resumen generado por Gemini]

=== TEXTO PROFESIONALIZADO ===

[Texto editado y profesionalizado por Gemini]

📸 Evidencia - Ejercicio 2
<img width="1254" height="741" alt="image" src="https://github.com/user-attachments/assets/cccf69f1-b1c3-4ce3-99ce-7945b495c08e" />


▶️ Ejercicio 3 - Chat de soporte con historial
Descripción
Este ejercicio implementa un sistema de chat para una tienda de tecnología.

El sistema utiliza:

system_instruction
Historial de conversación.
Few-Shot Learning.
Chat interactivo.
Memoria de las interacciones durante la sesión.
La IA actúa como un vendedor amable y puede responder preguntas relacionadas con productos tecnológicos de diferentes marcas y categorías.

Por ejemplo:

💻 Portátiles.
🖱️ Mouse.
⌨️ Teclados.
🎧 Audífonos.
📱 Celulares.
🖥️ Monitores.
🎮 Accesorios gaming.
📷 Cámaras.
🔌 Otros dispositivos tecnológicos.
Historial Few-Shot
Antes de iniciar la conversación se cargan ejemplos de preguntas y respuestas para orientar al modelo sobre la forma esperada de responder.

Por ejemplo:

Cliente:
¿Qué especificaciones tiene el TechBook Pro?

Vendedor:
El TechBook Pro cuenta con...

Estos ejemplos permiten proporcionar contexto al modelo antes de recibir las preguntas reales del usuario.

Ejecución
Ejecute:

python ejercicio3.py

A continuación aparecerá una interfaz similar a:

--- Chat de Soporte Tecnológico ---

Cliente:

Escriba cualquier pregunta relacionada con productos tecnológicos.

Para finalizar la conversación escriba:

finalizar

También puede utilizar:

salir

Ejemplo
Cliente: ¿Qué portátil me recomienda para programación?

Vendedor: Claro. Para programación le recomiendo un equipo
con al menos 16 GB de RAM, procesador de gama media o alta
y almacenamiento SSD...

Cliente: ¿Y qué mouse me recomienda para trabajar?

Vendedor: Para trabajo de oficina le recomiendo un mouse
ergonómico con conexión inalámbrica...

Cliente: finalizar

Vendedor: ¡Gracias por utilizar nuestro servicio!

📸 Evidencia - Ejercicio 3
<img width="1242" height="348" alt="image" src="https://github.com/user-attachments/assets/0108c50c-7599-4c2d-bb29-91907b8bd691" />

<img width="1252" height="407" alt="image" src="https://github.com/user-attachments/assets/69a573e3-ddbe-4a7a-87ec-7cd726de89f5" />