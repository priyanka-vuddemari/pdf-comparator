import fitz  # PyMuPDF
import json
 
def extract_text_from_pdf(pdf_path: str) -> str:
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
 
def load_json(json_path: str) -> dict:
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)
 
def compare_json_values_with_pdf(json_data: dict, pdf_text: str):
    missing = []
    for key, value in json_data.items():
        if str(value) not in pdf_text:
            missing.append((key, value))
    return missing
 
if __name__ == "__main__":
    # Replace with your actual file names
    pdf_file = "pdf_comparator/sample.pdf"
    json_file = "pdf_comparator/data.json"
 
    pdf_text = extract_text_from_pdf(pdf_file)
    json_data = load_json(json_file)
 
    result = compare_json_values_with_pdf(json_data, pdf_text)
 
    if not result:
        print("✅ All JSON values found in PDF.")
    else:
        print("❌ Missing values:")
        for key, value in result:
            print(f" - {key}: {value}")
 