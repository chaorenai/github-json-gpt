import json

def json_to_txt(json_file, txt_file):
    with open(json_file, 'r') as jf:
        data = json.load(jf)
    content = data.get('content', [])
    with open(txt_file, 'w') as tf:
        for line in content:
            tf.write(f"{line}")

json_to_txt('path/to/your/example.json', 'path/to/your/example.txt')