
from groq import Groq
from dotenv import load_dotenv
import os
import json


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)


def analysis(txt):
  prompt = f'''
You are a medical report summarizer.

Analyze the medical report text and return ONLY a valid JSON object.

Schema:

{{
  "report_type": "string",
  "patient_details": {{
    "name": "string",
    "age": "string",
    "sex": "string",
    "report_date": "string"
  }},
  "key_findings": ["string"],
  "abnormal_critical_values": [
    {{
      "parameter": "string",
      "value": "string",
      "reference_range": "string",
      "status": "normal|abnormal|critical"
    }}
  ],
  "diagnosis_impression": "string",
  "recommended_tests_medications_followups": ["string"],
  "patient_friendly_explanation": [
    "sentence1",
    "sentence2"
  ],
  "urgent_concerns": ["string"],
  "disclaimer": "This is AI-generated. Please consult your doctor."
}}

Rules:
- Return ONLY JSON.
- No markdown.
- No code blocks.
- No extra text.
- Use empty arrays when no data is available.
- Use 'Not mentioned in report' for missing fields.
- Do not hallucinate.
- Base all information strictly on the report.

Medical Report:
 {txt}'''


  completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=0.2,
  )
  
  response_text = completion.choices[0].message.content

  response_text = response_text.replace("```json", "")
  response_text = response_text.replace("```", "")

  try:

    start = response_text.find("{")
    end = response_text.rfind("}") + 1

    json_text = response_text[start:end]

    return json.loads(json_text)

  except Exception as e:

    print("JSON PARSE ERROR")
    print(response_text)

    return {
        "error": str(e),
        "raw_response": response_text
    }
