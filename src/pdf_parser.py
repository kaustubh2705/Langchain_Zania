import fitz  # PyMuPDF

class PDFParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        text = ""
        with fitz.open(self.pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text