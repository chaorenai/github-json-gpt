import os
from zipfile import ZipFile
import json

# Set the path for the newly uploaded zip file and the extraction target path
zip_path_animated_diff =  r"D:\Notes\GPTS\comfyui_GPTS\code\big\comfyui_controlnet_aux-main.zip"
extract_path_animated_diff =  r"D:\Notes\GPTS\comfyui_GPTS\code\big"
# List of file extensions for code files
code_extensions = ('.py', '.js', '.css', '.html','.md','.txt','json')

# Extract files
with ZipFile(zip_path_animated_diff, 'r') as zip_ref:
    zip_ref.extractall(extract_path_animated_diff)

# Recursively traverse the extraction directory, only getting file paths with specified extensions
file_paths_animated_diff = []
for root, directories, files in os.walk(extract_path_animated_diff):
    for filename in files:
        if filename.endswith(code_extensions):
            filepath = os.path.join(root, filename)
            relative_filepath = os.path.relpath(filepath, extract_path_animated_diff)
            file_paths_animated_diff.append(relative_filepath)

# Generate corresponding JSON for the new zip file, including filenames, directory structures, and complete code information
all_files_info_animated_diff = {}

for file_path in file_paths_animated_diff:
    try:
        # Read the content of each file
        full_path = os.path.join(extract_path_animated_diff, file_path)
        with open(full_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Use the file's relative path as the key, content as the value
        all_files_info_animated_diff[file_path] = file_content

    except Exception as e:
        # If there's an error reading the file or other operation, record the error message
        all_files_info_animated_diff[file_path] = "Error reading file: " + str(e)

# Save all file information as JSON, filename matches the zip filename (excluding extension)
json_animated_diff_filename =  r"D:\Notes\GPTS\comfyui_GPTS\code\big\comfyui_controlnet_aux-main.json"
with open(json_animated_diff_filename, 'w', encoding='utf-8') as json_file:
    json.dump(all_files_info_animated_diff, json_file, ensure_ascii=False, indent=4)
