# cli.py

from pdf_text_extractor import extract_text_from_pdf
from json_loader import load_json

pdf_path  = "/workspaces/pdf-comparator/pdf_comparator/sample.pdf"
json_path = "/workspaces/pdf-comparator/pdf_comparator/data.json"

pdf_text = extract_text_from_pdf(pdf_path)
json_data = load_json(json_path)

print("\n📄 PDF Extracted Text:\n", pdf_text[:500])  # print first 500 chars
print("\n📦 JSON Loaded Data:\n", json_data)
