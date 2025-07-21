from pdf_text_extractor import extract_text_from_pdf
from json_loader import load_json
from prompt_format import format_prompt
from llm_client import mock_call_llm
from response_parser import parse_ai_response



pdf_text = extract_text_from_pdf("/workspaces/pdf-comparator/pdf_comparator/sample.pdf")
json_data = load_json("/workspaces/pdf-comparator/pdf_comparator/data.json")
prompt = format_prompt(pdf_text, json_data)
print(prompt)

response = mock_call_llm(prompt)
# print("Mock AI Response:\n", response)

parsed = parse_ai_response(response)
print("✅ Matches:", parsed["match"])
print("❌ Mismatches:", parsed["mismatch"])
