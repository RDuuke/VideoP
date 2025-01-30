# VideoP - Procesamiento de Videos, Transcripción y Resumen Automático

**VideoP** es una herramienta en Python diseñada para procesar videos, dividirlos en fragmentos, convertirlos a audio, transcribirlos y generar resúmenes automáticos. 
Este proyecto es ideal para trabajar con videos largos, extraer su contenido en texto y obtener resúmenes concisos.

## Características Principales
- **División de videos:** Divide videos largos en fragmentos más pequeños.
- **Conversión a audio:** Convierte los fragmentos de video a archivos de audio en formato WAV.
- **Transcripción automática:** Utiliza el modelo Whisper de OpenAI para transcribir los archivos de audio a texto.
- **Generación de resúmenes:** Crea resúmenes en formato PDF a partir de las transcripciones.
- **Configuración flexible:** Permite personalizar la duración de los fragmentos, el modelo de transcripción y más.

## Requisitos del Sistema
- Python 3.8 o superior.
- FFmpeg instalado y disponible en el sistema.
- Dependencias de Python instaladas (ver requirements.txt).

## Instalación

1. **Clona Repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/VideoP.git
    cd VideoP
    ```
2. **Crea un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate     # En Windows
    ```
3. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4. Instala FFmpeg:
   - En Linux:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - En macOS (con Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - En Windows: Descarga FFmpeg desde [ffmpeg.org](ffmpeg.org) y agrega la ruta de `ffmpeg.exe` a las variables de entorno del sistema.

## Configuración
1. **Estructura del Proyecto:**
   - Coloca tus videos en la carpeta `videos/`.
   - Los fragmentos, audios, transcripciones y resúmenes se guardarán en la carpeta `data/`.
2. **Configuración de Whisper:**
   - El modelo de Whisper se descargará automáticamente la primera vez que ejecutes el proyecto.
   - Puedes cambiar el modelo en `config.py` (opciones: tiny, base, small, medium, large).
3. **Uso de OpenAI API (opcional):**
   1. **Obtén una clave de API**:
      - Regístrate en [OpenAI](https://platform.openai.com/signup/) y obtén tu clave de API.
      - La clave de API es necesaria para autenticar las solicitudes a la API de OpenAI.

   2. **Configura la clave de API**:
      - Abre el archivo `config.py` y agrega tu clave de API:
      ```python
      OPENAI_API_KEY = "tu_clave_de_api"
      USE_OPENAI_API = True
      ```
   3. **Instala la última versión de la biblioteca `openai`**:
      - Asegúrate de tener instalada la última versión de la biblioteca `openai`:
        ```bash
        pip install --upgrade openai
        ```
   4. **Modelos Disponibles**:
      - Puedes utilizar modelos como `gpt-3.5-turbo` o `gpt-4` para generar resúmenes o mejorar las transcripciones.
      - Cambia el modelo en `config.py` si es necesario:
        ```python
        OPENAI_MODEL = "gpt-3.5-turbo"  # Opciones: "gpt-3.5-turbo", "gpt-4", etc.
        ```
   5. **Ejemplo de Uso**:
      - Si `USE_OPENAI_API` está habilitado, el programa utilizará la API de OpenAI para generar resúmenes a partir de las transcripciones.
      - Asegúrate de tener conexión a Internet, ya que las solicitudes se envían a los servidores de OpenAI.

   6. **Costos**:
      - El uso de la API de OpenAI tiene un costo asociado. Consulta los precios en la [página de precios de OpenAI](https://openai.com/pricing).
      - Asegúrate de monitorear tu uso para evitar cargos inesperados.

## Uso
1. **Ejecuta el programa:**
    ````bash
    python main.py
    ````
2. **Selecciona un video:**
   - El programa mostrará una lista de videos disponibles en la carpeta `videos/`.
   - Ingresa el número del video que deseas procesar.
3. **Procesamiento automático:**
   - El video se dividirá en fragmentos.
   - Los fragmentos se convertirán a audio.
   - Los archivos de audio se transcribirán a texto.
   - Se generará un resumen en formato PDF.
4. **Resultados**
   - Los fragmentos de video se guardan en `data/fragments/`.
   - Los archivos de audio se guardan en `data/audios/`.
   - Las transcripciones se guardan en `data/transcripts/`.
   - El resumen se guarda en `data/summaries/`.

## Estructura del Proyecto
```
VideoP/
├── data/                   # Carpeta para almacenar fragmentos, audios, transcripciones y resúmenes
├── videos/                 # Carpeta para almacenar los videos de entrada
├── scripts/                # Módulos de Python para el procesamiento
│ ├── converter.py          # Conversión de fragmentos de video a audio
│ ├── splitter.py           # División de videos en fragmentos
│ ├── transcriber.py        # Transcripción de audio a texto
│ ├── summarizer.py         # Generación de resúmenes
├── main.py                 # Punto de entrada del programa
├── config.py               # Configuración del proyecto
├── requirements.txt        # Dependencias de Python
└── README.md               # Documentación del proyecto
```
---
## Dependencias
Las dependencias del proyecto se encuentran en requirements.txt. Para instalarlas, ejecuta:
````bash
pip install -r requirements.txt
````

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu feature (``git checkout -b feature/nueva-funcionalidad``).
3. Haz commit de tus cambios (``git commit -m 'Añadir nueva funcionalidad'``).
4. Haz push a la rama (``git push origin feature/nueva-funcionalidad``).
5. Abre un Pull Request.

## Notas Adicionales
- Asegúrate de que los videos estén en formato MP4.
- El proceso puede tardar varios minutos dependiendo del tamaño del video y el modelo de Whisper utilizado.
- Si encuentras algún problema, abre un issue en el repositorio.












