from docx import Document

doc = Document()

doc.add_paragraph("""
Medicine plays a vital role in improving the health and well-being of people around the world.
Medical professionals work tirelessly to diagnose, treat, and prevent diseases.
Advances in medical technology have made healthcare more accurate and effective.
Hospitals and clinics provide essential services to patients in need.
Vaccinations help protect communities from dangerous infectious diseases.
Medical research continues to discover new treatments and cures for various illnesses.
Doctors, nurses, and healthcare workers are crucial members of society.
Preventive care and regular checkups help individuals maintain good health.
The use of artificial intelligence is transforming modern medical practices.
Overall, medicine contributes significantly to increasing life expectancy and improving quality of life.
""")

doc.save("documents/testt.docx")

print("DOCX created")