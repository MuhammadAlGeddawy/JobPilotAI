from urllib.parse import urlparse
from .freelancer_scraper import extract_freelancer_description
from .linkedin_scraper import extract_linkedin_description
from .manual_input import prompt_manual_input

def get_job_description(url: str) -> str:
    domain = urlparse(url).netloc.lower()

    if "freelancer.com" in domain:
        return extract_freelancer_description(url)

    elif "linkedin.com" in domain:
        return extract_linkedin_description(url)

    else:
        return prompt_manual_input(source=domain)
