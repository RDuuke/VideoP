import logging
from pathlib import Path
from fpdf import FPDF

from config import USE_OPENAI_API, SUMMARY_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def summary_generate(transcription: str, session_name: str) -> str:
    transcription = Path(transcription)
    if not transcription.exists():
        logger.error(f"❌ El archivo {transcription} no existe.")
        return

    if not session_name or not isinstance(session_name, str):
        raise ValueError("El nombre de la sesión no es válido.")

    try:
        with open(transcription, "r", encoding="utf-8") as f:
            summary = f.read().strip()
    except Exception as e:
        logger.error(f"❌ Error al leer el archivo de transcripción: {e}")
        return

    if not summary:
        logger.error("❌ No hay contenido en la transcripción. No se puede generar resumen.")
        return

    if USE_OPENAI_API:
        import openai
        openai.api_key = "tu_api_key"  # Asegúrate de configurar tu API key
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Resume el siguiente texto:\n{summary}",
                max_tokens=150
            )
            summary = response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"❌ Error al generar el resumen con OpenAI: {e}")
            return

    summary_path = Path(SUMMARY_DIR) / session_name
    summary_path.mkdir(parents=True, exist_ok=True)

    summary_file = summary_path / "summary.pdf"

    if summary_file.exists():
        summary_file.unlink()  # Eliminar el archivo si ya existe

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=16, style="B")
    pdf.cell(0, 10, "Resumen de la Transcripción", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.output(str(summary_file))

    logger.info(f"✅  Resumen guardado en: {summary_file}")
    return str(summary_file)