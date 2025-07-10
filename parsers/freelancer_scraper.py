# parsers/job_scrapers/freelancer_scraper.py

import requests
from bs4 import BeautifulSoup
import re

def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def extract_freelancer_description(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    # Find the <fl-text class="Project-description">
    description_container = soup.find("fl-text", class_="Project-description")
    if not description_container:
        return "❌ Project description container not found."

    # Get inner <div> with actual text
    inner_div = description_container.find("div", class_="NativeElement")
    if not inner_div:
        return "❌ Inner description block not found."

    return clean_text(inner_div.get_text())

# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    test_url = "https://www.freelancer.com/projects/pcb-design-and-layout/Process-Optimization-Consultant-for/details"
    result = extract_freelancer_description(test_url)
    print("\n[FREELANCER] Extracted Description:\n")
    print(result)
