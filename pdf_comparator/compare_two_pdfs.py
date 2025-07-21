import fitz  # PyMuPDF
import json

def extract_text_from_pdf(pdf_path: str) -> str:
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def compare_pdfs(pdf1_path: str, pdf2_path: str):
    """
    Compare two PDFs by their text content.
    Returns:
        dict: {
            "identical": bool,
            "differences": list of (line_number, pdf1_line, pdf2_line)
        }
    """
    text1 = extract_text_from_pdf(pdf1_path)
    text2 = extract_text_from_pdf(pdf2_path)

    if text1 == text2:
        return {"identical": True, "differences": []}

    # Show line-by-line differences
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    differences = []
    for i, (l1, l2) in enumerate(zip(lines1, lines2), 1):
        if l1 != l2:
            differences.append((i, l1, l2))
    # Handle extra lines
    longer, which = (lines1, "pdf1") if len(lines1) > len(lines2) else (lines2, "pdf2")
    for i in range(len(lines1), len(lines2)):
        differences.append((i+1, "" if which == "pdf1" else longer[i], longer[i] if which == "pdf1" else ""))

    return {"identical": False, "differences": differences}

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Compare two PDFs by text content.")
    parser.add_argument("pdf1", help="First PDF file path")
    parser.add_argument("pdf2", help="Second PDF file path")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    result = compare_pdfs(args.pdf1, args.pdf2)
    if args.json:
        print(json.dumps(result))
    else:
        if result["identical"]:
            print("✅ The PDF files are identical (text content).")
        else:
            print("❌ The PDF files are different (text content).")
            print("\n--- Differences ---")
            for i, l1, l2 in result["differences"]:
                print(f"Line {i}:\n  PDF1: {l1}\n  PDF2: {l2}")