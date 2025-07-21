# gen-ai/parser.py
def parse_ai_response(response: str) -> dict:
    lines = response.strip().splitlines()
    results = {"match": [], "mismatch": []}
    for line in lines:
        if line.startswith("✅"):
            results["match"].append(line[1:].strip())
        elif line.startswith("❌"):
            results["mismatch"].append(line[1:].strip())
    return results
