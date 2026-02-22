import os
import re
import glob

# Ścieżka do katalogu Rasy
directory = r"a:\Coding\game\Rezeryum\Rasy"
os.chdir(directory)

# Wyrażenia regularne do usunięcia
patterns = [
    r"\(Rozwiązanie z \*Do Doprecyzowania\*\)\s*",
    r"\(rozwiązanie \*Do Doprecyzowania\*:.*?\)\s*",
    r"\(AI Prompt Guide\)\s*",
    r"\(AI Prompt\)\s*",
    r"\(AI Prompt.*?\)\s*",
    r"\(Dodano nową cechę\)\s*"
]

regexes = [re.compile(p) for p in patterns]

# Fiksy na zablokowane znaki polskie (Windows-1250 / UTF-8 garbling)
fixes = {
    "Ĺş": "ź", "Ĺ‚": "ł", "Ä…": "ą", "Ä™": "ę", "Ĺ›": "ś", "Ăł": "ó", "ĹĽ": "ż", "Ä‡": "ć", "Ĺ„": "ń",
    "Ĺą": "Ź", "Ĺ ": "Ł", "Ä„": "Ą", "Ä˜": "Ę", "Ĺš": "Ś", "Ă“": "Ó", "Ĺť": "Ż", "Ä†": "Ć", "Ĺƒ": "Ń",
    "â€“": "–", "â€ž": "„", "â€ ": "”"
}

# Wzorzec na wypadek utrwalonego UTF-8 śmiecia z Do Doprecyzowania
regexes.append(re.compile(r"\(RozwiÄ…zanie z \*Do Doprecyzowania\*\)\s*"))
regexes.append(re.compile(r"\(rozwiÄ…zanie \*Do Doprecyzowania\*:.*?\)\s*"))


files_processed = []

for filepath in glob.glob("*.md"):
    # Odczyt jako UTF-8, używając surrogateescape żeby nie zgubić danych
    with open(filepath, "r", encoding="utf-8", errors="surrogateescape") as f:
        content = f.read()

    original_content = content
    
    # Naprawa znaków
    for bad, good in fixes.items():
        content = content.replace(bad, good)
        
    # Usuwanie tagów   
    for r in regexes:
        content = r.sub("", content)
        
    # Zapis z prawidłowym kodowaniem
    if content != original_content:
        # Prawdziwy plik UTF-8 bez BOM
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        files_processed.append(filepath)

print("Processed files:")
for f in files_processed:
    print(f"- [{f}] - Usunięto meta-tagi.")
