# Helper functions (e.g., URL validation, HTML parsing)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all('a', href=True):
        full_url = urljoin(base_url, tag['href'])
        links.add(full_url)
    return links

