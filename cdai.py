
from groq import Groq
from dotenv import load_dotenv
import os
import json


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)


def analysis(txt):
  prompt = f'''
  You are a strict, senior clinical pathologist reviewing a medical lab report.
  Your job is to extract ONLY what is explicitly written in the report text.
 
  CRITICAL RULES — VIOLATION IS NOT ACCEPTABLE:
  1. NEVER infer, estimate, or fabricate any test value. If a result field is blank, empty, or not present in the text, the value MUST be "Not reported".
  2. If the report says "Result/s to follow" or "Interim" or "Pending", those tests have NO results yet. Do NOT guess or fill in values.
  3. Only include a test in abnormal_critical_values if BOTH the result value AND reference range are explicitly stated in the report text.
  4. For status: only mark "abnormal" if the value clearly falls outside the stated reference range. Only mark "critical" if the report itself uses words like "critical", "panic", or "urgent". Otherwise mark "normal".
  5. hsCRP of 1.00 mg/L with reference <1.00 is ABNORMAL (borderline/average cardiovascular risk), NOT normal.
  6. Do NOT include any parameter where the result value is blank or missing in the report.
  7. Patient name, age, sex, and date must be copied exactly as written. Do not say "Not mentioned" if it appears anywhere in the report text.
  8. key_findings must only describe what is actually reported with actual values — never describe tests that have no result yet.
  9. If the report is interim/partial, state that clearly in diagnosis_impression.
  10. patient_friendly_explanation must be based only on actual reported values — if most results are pending, say so plainly.
 
  Return ONLY a valid JSON object matching this schema exactly:
 
  {{
  "report_type": "string — exact test panel name from report",
  "patient_details": {{
    "name": "string — exact name from report",
    "age": "string — exact age from report",
    "sex": "string — exact sex/gender from report",
    "report_date": "string — exact date from report"
  }},
  "key_findings": [
    "Only list tests that have an actual numeric result. Format: Test Name: value unit (reference: range). Skip any test with no result."
  ],
  "abnormal_critical_values": [
    {{
      "parameter": "exact test name",
      "value": "exact numeric value with unit as written in report — NEVER leave blank",
      "reference_range": "exact reference range as written in report",
      "status": "normal|abnormal|critical"
    }}
  ],
  "diagnosis_impression": "string — if interim report with pending results, say so. Do not diagnose from missing data.",
  "recommended_tests_medications_followups": [
    "List any pending tests mentioned as 'Result/s to follow'. List any follow-up instructions from the report."
  ],
  "patient_friendly_explanation": [
    "Plain English sentences about ONLY the tests that have actual results. If most tests are pending, tell the patient clearly that results are not yet available and they should wait for the complete report."
  ],
  "urgent_concerns": [
    "Only list if a value is critically abnormal or the report itself flags urgency. Use empty array if nothing urgent."
  ],
  "disclaimer": "This is AI-generated. Results shown are based strictly on reported values. Please consult your doctor for interpretation."
  }}
 
FINAL CHECK BEFORE RESPONDING:
- Did you invent any number not present in the report text? If yes, remove it.
- Did you mark a blank result as reported? If yes, change to Not reported.
- Is the report interim? If yes, mention pending tests in recommended_tests_medications_followups.
- Did you copy the patient name exactly? If it is in the report, it must appear in your response.
 
Medical Report Text:
 {txt}'''


  completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=0.1,
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
