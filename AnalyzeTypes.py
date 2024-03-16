import json
import os

def load_json_content(file_path):
    """Load JSON content from a specified file path."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_file_extensions(data, extensions=None):
    """Recursively extract file extensions from nested JSON structures."""
    if extensions is None:
        extensions = set()

    if isinstance(data, dict):
        for key, value in data.items():
            _, ext = os.path.splitext(key)
            if ext:  # If there is an extension, add it to the set
                extensions.add(ext.lower())
            extract_file_extensions(value, extensions)  # Recursive call to handle nested dictionaries
    elif isinstance(data, list):
        for item in data:
            extract_file_extensions(item, extensions)  # Recursive call to handle each item in lists

    return extensions

# Replace the following paths with your actual file paths
file_path_1 = r"D:\Notes\GPTS\comfyui_GPTS\code\gpts\stable-diffusion-webui-master.json"
file_path_2 = r"D:\Notes\GPTS\comfyui_GPTS\code\gpts\InstantID_IPAdapter_segment_AnimateDiff_LDSR_inpaint.json"
file_path_3 = r"D:\Notes\GPTS\comfyui_GPTS\code\gpts\IPA_SD_WAS.json"

data_1 = load_json_content(file_path_1)
data_2 = load_json_content(file_path_2)
data_3 = load_json_content(file_path_3)

extensions_1 = extract_file_extensions(data_1)
extensions_2 = extract_file_extensions(data_2)
extensions_3 = extract_file_extensions(data_3)

print("File extensions in the first JSON file:", extensions_1)
print("File extensions in the second JSON file:", extensions_2)
print("File extensions in the third JSON file:", extensions_3)
