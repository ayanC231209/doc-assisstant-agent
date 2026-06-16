from pypdf import PdfReader
from docx import Document


def read_document(path):

    # TXT
    if path.endswith(".txt"):

        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    # PDF
    elif path.endswith(".pdf"):

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    # DOCX
    elif path.endswith(".docx"):

        doc = Document(path)

        text = "\n".join(
            [paragraph.text for paragraph in doc.paragraphs]
        )

        return text

    else:
        raise Exception(
            "Unsupported file type"
        )