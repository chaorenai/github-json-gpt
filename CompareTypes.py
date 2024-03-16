import json

# Replace 'path_to_file' with the actual path to your JSON file
with open(r"D:\Notes\GPTS\comfyui_GPTS\1\a-person-mask-generator-main.json", 'r', encoding='utf-8') as file:
    data_main = json.load(file)

with open(r"D:\Notes\GPTS\comfyui_GPTS\1\merged_ComfyUI_files.json", 'r', encoding='utf-8') as file:
    data_main2 = json.load(file)

# Check if all specified types exist
extensions = ['.py', '.js', '.css', '.html', '.md', '.txt', 'json']
main_extensions = {ext: any(key.endswith(ext) for key in data_main) for ext in extensions}

# Identify size differences
main_size = sum(len(content) for content in data_main.values())
main2_size = sum(len(content) for content in data_main2.values())
size_difference = main2_size - main_size

# Identify extra content in the larger file
extra_content = {key: len(value) for key, value in data_main2.items() if key not in data_main}

print(f"Does comfyui_segment_anything-main.json include all .py, .js, .css, .html files? {main_extensions}")
print(f"Size difference between the two files: {size_difference}")
print(f"Extra content in the larger file: {extra_content}")
