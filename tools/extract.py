import pdfplumber
import docx


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = '\n'.join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text


def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text


def extract_text(file):
    if file.type == "application/pdf":
        resume = extract_text_from_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume = extract_text_from_docx(file)
    elif file.type == "text/plain":
        resume = file.read().decode("utf-8")
    return resume
