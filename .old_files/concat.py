import os

with open('temp_all_text.txt', 'w', encoding='utf-8') as out_f:
    for root, dirs, files in os.walk('.'):
        if '.old_files' in root.replace('\\', '/'):
            continue
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as in_f:
                    out_f.write(f"\n--- FILE: {path} ---\n")
                    out_f.write(in_f.read())
