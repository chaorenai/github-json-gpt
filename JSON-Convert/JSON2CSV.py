import pandas as pd

def json_to_csv(json_file, csv_file):
    df = pd.read_json(json_file, lines=True)
    df.to_csv(csv_file, index=False)

json_to_csv('path/to/your/example.json', 'path/to/your/example.csv')