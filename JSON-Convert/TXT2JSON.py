import json

def txt_to_json(txt_file, json_file):
    with open(txt_file, 'r') as tf:
        content = tf.readlines()
    data = {'content': content}
    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)

txt_to_json(r"C:\Users\sunny\Desktop\text.txt", r"C:\Users\sunny\Desktop\text.json")