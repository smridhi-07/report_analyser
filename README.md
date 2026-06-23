
Readme · MD
# 🏥 Clinical Report Analyser
 
An AI-powered web app that analyses medical lab reports (PDFs) and returns a structured, patient-friendly summary — flagging abnormal values, key findings, and urgent concerns.
 
**Live Demo:** [smridhi-07.github.io/report_analyser](https://smridhi-07.github.io/report_analyser/)
 
---
 
## What it does
 
- Upload any medical lab report as a PDF
- Extracts text directly from the PDF (no OCR needed for digital reports)
- Sends the report to an LLM for clinical analysis
- Returns a structured summary including:
  - Patient details
  - Key findings with values and reference ranges
  - Abnormal / critical values flagged clearly
  - Diagnosis impression
  - Plain-language explanation for patients
  - Recommended follow-ups
  - Urgent concerns
---
 
## Tech Stack
 
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript (vanilla) |
| Backend | Python, FastAPI |
| PDF Extraction | PyMuPDF (fitz) |
| AI Analysis | Groq API (Llama 4 Scout) |
| Frontend Hosting | GitHub Pages |
| Backend Hosting | Render |
 
---
 
## Project Structure
 
```
report_analyser/
├── main.py          
├── cdai.py         
├── requirements.txt 
├── index.html      
├── .env             
└── .gitignore
```
