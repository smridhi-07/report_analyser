from imgtotxt import ocr_slides
from groq import Groq
from dotenv import load_dotenv
import os
import json
import base64

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)


def analysis(txt):
  
  prompt = f'''You are a medical report summarizer. When given a medical report

   1. Identify the report type and patient details (age, sex, date).
   2. List the key findings in simple, clear language.
   3. Flag any ABNORMAL or CRITICAL values in bold.
   4. State the diagnosis or doctor's impression in one sentence.
   5. List any recommended tests, medications, or follow-ups.
   6. Write a 2-sentence plain-English explanation for the patient.
   7. Note any urgent concerns that need immediate attention.
   8. If any information is missing, write Not mentioned in report.
   9. Do not guess or add information not found in the report.
   10. End with: This is AI-generated. Please consult your doctor.
   you are provided with medical report's images {txt}'''


  completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=1,
  )
  
  response_text = completion.choices[0].message.content
  print(response_text)

x=ocr_slides()
for i in range(len(x)):
  analysis(x[i])
