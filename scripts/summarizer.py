import os
from config import USE_OPENAI_API, SUMMARY_DIR
from fpdf import FPDF


def summary_generate(transcription: str, session_name: str):
    with open(transcription, "r", encoding="utf-8") as f:
        summary = f.read().strip()

    if not summary:
        print("❌ No hay contenido en la transcripción. No se puede generar resumen.")
        return

    if USE_OPENAI_API:
       pass

    summary_path = os.path.join(SUMMARY_DIR, session_name)
    os.makedirs(summary_path, exist_ok=True)

    summary_file = os.path.join(summary_path, "summary.pdf")

    if os.path.exists(summary_file):
        os.remove(summary_file)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.output(summary_file)

    print(f"✅  Resumen guardado en: {summary_file}")