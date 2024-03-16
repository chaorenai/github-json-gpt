import pdfplumber
import json

def pdf_to_json(pdf_file, json_file):
    with pdfplumber.open(pdf_file) as pdf:
        content = [page.extract_text() for page in pdf.pages]
    data = {'content': content}
    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)

pdf_to_json('path/to/your/example.pdf', 'path/to/your/example.json')