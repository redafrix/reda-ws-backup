#!/usr/bin/env python3
import subprocess
import sys
import re

def main():
    # Extract text from PDF
    try:
        text = subprocess.check_output(["pdftotext", "main.pdf", "-"]).decode("utf-8")
    except Exception as e:
        print(f"Error running pdftotext: {e}")
        sys.exit(1)

    # 1. Slide count verification
    page_count = text.count('\x0c')
    print(f"Detected page count: {page_count}")
    if page_count != 9:
        print(f"ERROR: Slide count is {page_count}, expected exactly 9.")
        sys.exit(1)
    else:
        print("PASS: Slide count is exactly 9.")

    # 2. Forbidden terms check
    forbidden = ["TopK8", "unc_topk8", "OOD", "FA", "D@25", "AUC", "reset seeds", "ckpt"]
    found_forbidden = []
    
    for term in forbidden:
        pattern = r'\b' + re.escape(term) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            found_forbidden.append(term)
            
    if found_forbidden:
        print(f"ERROR: Found forbidden terms: {found_forbidden}")
        lines = text.split('\n')
        for i, line in enumerate(lines):
            for term in found_forbidden:
                pattern = r'\b' + re.escape(term) + r'\b'
                if re.search(pattern, line, re.IGNORECASE):
                    print(f"  Line {i+1}: {line}")
        sys.exit(1)
    else:
        print("PASS: No forbidden terms found.")

    # 3. Check ACE usage count
    ace_matches = re.findall(r'\bACE\b', text, re.IGNORECASE)
    ace_count = len(ace_matches)
    print(f"ACE term count: {ace_count}")
    if ace_count > 1:
        print(f"ERROR: ACE appears {ace_count} times, must be at most once.")
        sys.exit(1)
    else:
        print("PASS: ACE appears at most once.")

    # 4. Check RND presence
    rnd_matches = re.findall(r'\bRND\b', text, re.IGNORECASE)
    rnd_count = len(rnd_matches)
    print(f"RND term count: {rnd_count}")
    if rnd_count == 0:
        print("ERROR: RND (Random Network Distillation) is not mentioned in the presentation.")
        sys.exit(1)
    else:
        print("PASS: RND is mentioned correctly.")

    # 5. Check for French words
    french_words = ["résultats", "données", "détecteur", "temps réel", "contexte", "modèle", "présentation"]
    found_french = []
    for word in french_words:
        if word in text.lower():
            found_french.append(word)
    if found_french:
         print(f"WARNING: Possible French words found: {found_french}")
    else:
         print("PASS: No common French words found.")

    print("Verification completed successfully.")

if __name__ == "__main__":
    main()
