from docx import Document
import json

def doc_to_json(doc_file, json_file):
    doc = Document(doc_file)
    data = {'content': [para.text for para in doc.paragraphs]}
    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)

doc_to_json('path/to/your/example.docx', 'path/to/your/example.json')