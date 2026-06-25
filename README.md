
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
## How it works
 
```
User uploads PDF
      ↓
FastAPI receives file
      ↓
PyMuPDF extracts text from PDF pages
      ↓
Text sent to Groq LLM with clinical prompt
      ↓
LLM returns structured JSON
      ↓
Frontend renders formatted medical summary
```
 
---
 
## Setup (Local)
 
### Prerequisites
- Python 3.10+
- A [Groq API key](https://console.groq.com)
### 1. Clone the repo
```bash
git clone https://github.com/smridhi-07/report_analyser.git
cd report_analyser
```
 
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
 
### 3. Set up environment variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```
 
### 4. Run the backend
```bash
uvicorn main:app --reload --port 8000
```
 
### 5. Open the frontend
Open `index.html` via Live Server (VS Code extension) or any local HTTP server. Then set the API endpoint to:
```
http://localhost:8000/analyse
```
