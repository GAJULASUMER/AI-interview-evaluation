from datetime import datetime
from fpdf import FPDF


def generate_report(payload: dict, output_path: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Interview Report", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Generated: {datetime.utcnow().isoformat()}", ln=True)

    for key, value in payload.items():
        pdf.multi_cell(0, 8, txt=f"{key}: {value}")

    pdf.output(output_path)
    return output_path
