# cv_parser.py

import re
from .file_reader import read_file
from .config import SECTION_HEADERS


def extract_sections(text):
    sections = {}
    current = None
    lines = text.splitlines()

    for line in lines:
        header = line.strip().lower().rstrip(":")
        if header in SECTION_HEADERS:
            current = header
            sections[current] = []
        elif current:
            sections[current].append(line.strip())

    # Join lines back into paragraphs
    for key in sections:
        sections[key] = "\n".join(sections[key]).strip()

    return sections

def extract_contact_info(text):
    email = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone = re.search(r"(\+\d{1,3})?\s?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}", text)

    return {
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None
    }

def parse_cv(path):
    text = read_file(path)
    sections = extract_sections(text)
    contact = extract_contact_info(text)
    return {
        "raw_text": text,
        "contact_info": contact,
        "sections": sections
    }

def to_prompt_text(parsed_cv):
    contact = parsed_cv["contact_info"]
    sections = parsed_cv["sections"]

    blocks = []
    if contact["email"]:
        blocks.append(f"Email: {contact['email']}")
    if contact["phone"]:
        blocks.append(f"Phone: {contact['phone']}")

    for key, value in sections.items():
        title = key.replace("_", " ").title()
        blocks.append(f"\n{title}:\n{value}")

    return "\n".join(blocks)
