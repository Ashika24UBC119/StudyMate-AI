import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF file.

    Parameters:
        pdf_file: Uploaded PDF from Streamlit

    Returns:
        Extracted text as a string
    """

    text = ""

    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()

    return text
