import streamlit as st
import os

from document_reader import read_document
from rewrite import rewrite_document
from summary import summarize_document
from qa import ask_question
from document_writer import save_docx


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Assistant")

st.write(
    "Upload a TXT, PDF, or DOCX document and use AI tools."
)

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["txt", "pdf", "docx"]
)

if uploaded_file:

    # Save uploaded file temporarily
    temp_path = uploaded_file.name

    with open(temp_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    # Read document
    text = read_document(temp_path)

    st.subheader("📖 Document Preview")

    st.text_area(
        "",
        text,
        height=250
    )

    st.divider()

    col1, col2 = st.columns(2)

    # -------------------
    # Rewrite
    # -------------------
    with col1:

        if st.button("🔄 Rewrite Document"):

            with st.spinner("Rewriting document..."):

                rewritten_text = rewrite_document(text)

                save_docx(
                    rewritten_text,
                    "output/rewritten.docx"
                )

            st.subheader("Rewritten Document")

            st.write(rewritten_text)

            with open(
                "output/rewritten.docx",
                "rb"
            ) as file:

                st.download_button(
                    label="⬇ Download Rewritten DOCX",
                    data=file,
                    file_name="rewritten.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

    # -------------------
    # Summary
    # -------------------
    with col2:

        if st.button("📝 Summarize Document"):

            with st.spinner("Generating summary..."):

                summary = summarize_document(text)

            st.subheader("Summary")

            st.write(summary)

    st.divider()

    st.subheader("❓ Ask Questions About Document")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner("Thinking..."):

                answer = ask_question(
                    text,
                    question
                )

            st.subheader("Answer")

            st.write(answer)

        else:

            st.warning(
                "Please enter a question."
            )