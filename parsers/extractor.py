import os
from parsers.pdf_reader import read_pdf
from parsers.docx_reader import read_docx
from parsers.cleaner import clean_text

def extract_resume(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        raw = read_pdf(file_path)
    elif ext == ".docx":
        raw = read_docx(file_path)
    else:
        raise ValueError("Only .pdf or .docx supported")

    cleaned = clean_text(raw)
    return cleaned