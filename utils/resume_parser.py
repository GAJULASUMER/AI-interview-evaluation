import os
import re
from PyPDF2 import PdfReader
import docx2txt


def extract_resume_text(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if ext in {".docx", ".doc"}:
        return docx2txt.process(path) or ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def extract_skills(text):
    skill_bank = {
        "python", "java", "javascript", "sql", "mysql", "flask", "django", "react", "node", "aws",
        "docker", "kubernetes", "ml", "nlp", "pandas", "numpy", "git", "rest", "api", "html", "css"
    }
    tokens = set(re.findall(r"[a-zA-Z+#.]{2,}", text.lower()))
    return sorted(tokens.intersection(skill_bank))
