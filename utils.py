# Helper functions (e.g., URL validation, HTML parsing)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all('a', href=True):
        full_url = urljoin(base_url, tag['href'])
        links.add(full_url)
    return links

def is_same_domain(url, domain):
    return urlparse(url).netloc == domain

def save_results(urls, filename="crawled_urls.txt"):
    with open(filename, "w") as f:
        for url in sorted(urls):
            f.write(url + "\n")