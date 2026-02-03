file_path = "markdown/class1.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

file_name1 = "sample1.md"
print(file_name1.endswith(".md"))  # True
file_name2 = "document.txt"
print(file_name2.endswith(".md"))  # False

import os

folder_path = "pages"
files = os.listdir(folder_path)
print(files)

file_name2 = "document.txt"
print(file_name2.endswith(".md"))  # False

import os

folder_path = "markdown"
files = os.listdir(folder_path)
selected_files = []
for file in files:
    if file.endswith(".md"):
        selected_files.append(file[:-3])  # remove .md

print(selected_files)
