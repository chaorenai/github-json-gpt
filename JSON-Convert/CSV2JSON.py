import pandas as pd

def csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', lines=True)

csv_to_json('path/to/your/example.csv', 'path/to/your/example.json')