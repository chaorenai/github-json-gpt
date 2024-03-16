import json

# Specify the path to your JSON file
json_file_path = r"D:\Notes\GPTS\comfyui_GPTS\prompt\prompt.json"  # Replace with the actual path to your JSON file

def analyze_json_content(data):
    file_counts = {}
    file_sizes = {}

    # Function to process each item (assuming it's a dictionary)
    def process_item(item):
        for key in item.keys():
            # Count file types
            ext = key.split('.')[-1]
            file_counts[ext] = file_counts.get(ext, 0) + 1
            # Calculate file sizes
            file_sizes[key] = len(item[key])

    # Check if the data is a dictionary
    if isinstance(data, dict):
        process_item(data)
    # Check if the data is a list of dictionaries
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        for item in data:
            process_item(item)
    else:
        print("The JSON structure is not as expected. Please check the JSON file.")
        return

    print("File counts:", sorted(file_counts.items(), key=lambda x: x[1], reverse=True))

    # Sort and print the top ten largest files
    sorted_files = sorted(file_sizes.items(), key=lambda item: item[1], reverse=True)[:10]
    for file, size in sorted_files:
        print(f"{file}: {size} bytes")

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

analyze_json_content(data)
