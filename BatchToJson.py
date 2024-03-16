import os
from zipfile import ZipFile
import json

# Set the path to the folder containing zip files
zip_files_folder = r"D:\Notes\GPTS\comfyui_GPTS\code\big"
code_extensions = ('.py', '.js', '.css', '.html', '.md', '.txt', '.json')

# Iterate over all zip files in the folder
for zip_file_name in os.listdir(zip_files_folder):
    if zip_file_name.endswith('.zip'):
        zip_path = os.path.join(zip_files_folder, zip_file_name)
        extract_path = os.path.join(zip_files_folder, zip_file_name[:-4])  # Remove the .zip suffix
        
        # Extract the zip files
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        
        # Recursively traverse the extracted directory, only retrieving the paths of files with specified extension
        file_paths = []
        for root, directories, files in os.walk(extract_path):
            for filename in files:
                if filename.endswith(code_extensions):
                    filepath = os.path.join(root, filename)
                    relative_filepath = os.path.relpath(filepath, extract_path)
                    file_paths.append(relative_filepath)
        
        # Build a dictionary containing file paths and contents
        all_files_info = {}
        for file_path in file_paths:
            try:
                full_path = os.path.join(extract_path, file_path)
                with open(full_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                all_files_info[file_path] = file_content
            except Exception as e:
                all_files_info[file_path] = "Error reading file: " + str(e)
        
        # Save as a JSON file, with the file name same as the original zip file
        json_filename = os.path.join(zip_files_folder, zip_file_name[:-4] + '.json')
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(all_files_info, json_file, ensure_ascii=False, indent=4)
