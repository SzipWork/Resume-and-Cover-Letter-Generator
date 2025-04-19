from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from io import BytesIO
from xhtml2pdf import pisa
from docx import Document


load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#STREAMLIT DOCUMENTATIONS
st.title("Resume & Cover Letter Generator")

name = st.text_input("Your Name")
job_title = st.text_input("Target Job Title")
skills = st.text_area("Your Skills")
experience = st.text_area("Brief Work Experience")
job_description = st.text_area("Job Description / Role Details")

generated_text = ""

if st.button("Generate"):
    with st.spinner("Generating documents..."):
        prompt = f"""
You are an expert resume and cover letter writer.

Create a tailored resume and a professional cover letter for the following person:

Name: {name}
Target Job Title: {job_title}
Skills: {skills}
Experience: {experience}

Job Description: {job_description}

Write the resume first, followed by the cover letter.
"""
        response = llm.invoke(prompt)
        generated_text = response.content

        st.markdown("---")
        st.markdown(generated_text)

#EXPORT FUNCTIONS
def convert_to_pdf(text):
    html = f"<pre>{text}</pre>"
    pdf = BytesIO()
    pisa.CreatePDF(html, dest=pdf)
    return pdf

def convert_to_docx(text):
    doc = Document()
    for line in text.split('\n'):
        doc.add_paragraph(line)
    output = BytesIO()
    doc.save(output)
    return output

#BUTTONS
if generated_text:
    col1, col2 = st.columns(2)

    with col1:
        pdf_file = convert_to_pdf(generated_text)
        st.download_button("Download PDF", data=pdf_file.getvalue(),
                           file_name="Resume_CoverLetter.pdf", mime="application/pdf")

    with col2:
        docx_file = convert_to_docx(generated_text)
        st.download_button("Download DOCX", data=docx_file.getvalue(),
                           file_name="Resume_CoverLetter.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")