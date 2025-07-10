# file_reader.py

import fitz  
import docx

def read_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_file(path):
    if path.endswith(".pdf"):
        return read_pdf(path)
    elif path.endswith(".docx"):
        return read_docx(path)
    elif path.endswith(".txt"):
        return read_txt(path)
    else:
        raise ValueError("Unsupported file type. Use .pdf, .docx, or .txt")
