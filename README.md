# Resume and Cover Letter Generator

This is a Streamlit-based web application that generates a tailored resume and cover letter using Google's Gemini 1.5 Pro model via LangChain. Users input basic details such as their name, target job title, skills, experience, and a job description. The application returns a professionally written resume followed by a cover letter, which can be downloaded as either PDF or DOCX.

---

## Features

- Accepts user inputs for resume personalization.
- Generates both resume and cover letter in a single response.
- Uses Gemini 1.5 Pro for natural language generation.
- Allows download of the generated content in:
  - PDF format
  - DOCX format

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Environment Variables
```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### Usage
```bash
streamlit run rc_gen.py
```
Once the app launches in your browser:

Fill in the form fields:

- Name
- Target Job Title
- Skills
- Work Experience
- Job Description

Click Generate to create the resume and cover letter.

Download the result using the Download PDF or Download DOCX buttons.

### File Structure
```bash
rc_gen.py           # Main Streamlit application
.env                # Environment variable file (excluded from version control)
requirements.txt    # List of required dependencies
```

### Notes
- Text generation is handled using LangChain’s invoke() method with Gemini 1.5 Pro.
- The generated content is styled as plain text. You may further style the resume or cover letter after downloading.
- PDF generation uses xhtml2pdf, while DOCX conversion uses python-docx.

### Contributing
Feel free to submit issues or pull requests to enhance this project.
