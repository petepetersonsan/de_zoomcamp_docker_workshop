import os
from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Fiiles in {current_dir}:")

for file_path in current_dir.iterdir():
    #file_path = file_path.split('/')[-1]
    if file_path.name == current_file:
        continue
    print(f"filename is {file_path.name}")
    if file_path.is_file():
        content = file_path.read_text(encoding='utf-8').strip()
        #if content != '':
        print(f"content is {content}")



