from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text

# Exemple d'utilisation
pdf_path = "example.pdf"
text = extract_text_from_pdf(pdf_path)
print(text)
