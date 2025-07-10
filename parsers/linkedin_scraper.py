import requests
from bs4 import BeautifulSoup

def extract_linkedin_description(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    container = soup.find("div", class_="description__text description__text--rich")
    if not container:
        print("❌ Could not find job description container.")
        return ""

    # Extract visible text
    description = container.get_text(separator="\n", strip=True)
    return description


# Example usage
if __name__ == "__main__":
    url = "https://www.linkedin.com/jobs/view/4250945120/?alternateChannel=search&eBP=NOT_ELIGIBLE_FOR_CHARGING&refId=t9m1GZ0Y1UtdlG36GdH%2Bpg%3D%3D&trackingId=C%2BSJCGA42%2F0nN%2BG6bZkUVw%3D%3D"
    description = extract_linkedin_description(url)
    print("[LINKEDIN] Extracted Description:\n")
    print(description)
