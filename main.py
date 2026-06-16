from document_reader import read_document
from rewrite import rewrite_document
from summary import summarize_document
from qa import ask_question
from document_writer import save_docx

file_path = input(
    "Enter document path: "
)

text = read_document(
    file_path
)

print("\n===== DOCUMENT ASSISTANT =====")
print("1. Rewrite Document")
print("2. Summarize Document")
print("3. Ask Question")

choice = input("\nChoose an option: ")

if choice == "1":

    result = rewrite_document(text)

    print("\n===== REWRITTEN DOCUMENT =====\n")
    print(result)

    from document_writer import save_docx

    save_docx(
        result,
        "output/rewritten.docx"
    )

    print("\nDOCX file saved successfully!")

elif choice == "2":

    result = summarize_document(text)

    print("\n===== SUMMARY =====\n")
    print(result)

elif choice == "3":

    question = input("\nEnter your question: ")

    result = ask_question(
        text,
        question
    )

    print("\n===== ANSWER =====\n")
    print(result)

else:
    print("Invalid choice")