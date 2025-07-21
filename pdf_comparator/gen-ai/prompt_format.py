def format_prompt(pdf_text: str, json_data: dict, template_name: str = "Default") -> str:
    fields = "\n".join([f"{k}: {v}" for k, v in json_data.items()])
    return f"""
You are an AI validator for document templates.

Template: {template_name}
PDF Content:
---
{pdf_text}
---

Expected Fields from JSON:
{fields}

Check if all fields exist and are correctly placed. Respond with discrepancies, if any.
"""
