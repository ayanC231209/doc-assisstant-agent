from docx import Document


def save_docx(text, filename):

    doc = Document()

    doc.add_paragraph(text)

    doc.save(filename)