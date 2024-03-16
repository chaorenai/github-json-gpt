import json
import os

# Specify the target folder path
folder_path = r"D:\Notes\GPTS\comfyui_GPTS\1"  # Replace with your folder path

# Get all JSON file paths in the folder
json_file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]

# Dictionary for storing the contents of each file
json_contents = {}

# Iterate through each JSON file path, read, and parse the JSON content
for file_path in json_file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding as UTF-8
        file_name = os.path.basename(file_path).replace('.json', '')  # Get the file name as the key
        json_contents[file_name] = json.load(file)  # Directly parse the file content into JSON

# Combine the JSON contents of all files into a single dictionary
merged_json = json_contents

# Specify the path for the merged JSON file
merged_file_path = os.path.join(folder_path, "merged_ComfyUI_files.json")  # Save the merged file to the specified path

# Save the merged JSON to a new file
with open(merged_file_path, 'w', encoding='utf-8') as file:  # Specify encoding as UTF-8
    json.dump(merged_json, file, ensure_ascii=False, indent=4)  # Save content in JSON format

print("Merged file path: ", merged_file_path)
