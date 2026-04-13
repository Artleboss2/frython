import os
import sys
import re
from collections import Counter

PYTHON_KEYWORDS = [
    'if', 'else', 'elif', 'for', 'while', 'def', 'class', 
    'import', 'from', 'return', 'try', 'except', 'finally', 
    'with', 'as', 'lambda', 'None', 'True', 'False'
]

def analyze_frython_files():
    found_keywords = Counter()
    errors_found = False

    for root, _, files in os.walk("."):
        if ".github" in root or "venv" in root:
            continue
            
        for file in files:
            if file.endswith(".fry"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        for kw in PYTHON_KEYWORDS:
                            if re.search(rf'\b{kw}\b', line):
                                found_keywords[kw] += 1
                                print(f"❌ {file}:{i} -> {kw}")
                                errors_found = True

    if found_keywords:
        print("\n--- PRIORITÉS DE TRADUCTION ---")
        for kw, count in found_keywords.most_common():
            print(f"⭐ {kw}: {count} occurrences")
    
    return errors_found

if __name__ == "__main__":
    if analyze_frython_files():
        sys.exit(1)
    else:
        print("✅ 100% Frython")
        sys.exit(0)
