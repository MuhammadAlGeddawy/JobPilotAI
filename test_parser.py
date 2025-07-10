from parsers.cv_parser import parse_cv
from parsers.file_reader import read_file

cv_text = read_file("Muhammad Al-Geddawy - CV.pdf")  # Make sure this file is in the project root or adjust path
parsed = parse_cv(cv_text)

for section, content in parsed.items():
    print(f"\n--- {section.upper()} ---")
    print(content.strip())
