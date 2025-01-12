import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

class WebCrawler:
    def __init__(self, start_url, max_depth):
        self.start_url = start_url
        self.max_depth = max_depth
        self.domain = urlparse(start_url).netloc
        self.visited = set()
        self.queue = deque([(start_url, 0)])  # (url, depth)

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch {url}: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
        return None

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for tag in soup.find_all('a', href=True):
            full_url = urljoin(base_url, tag['href'])
            links.add(full_url)
        return links

    def is_same_domain(self, url):
        return urlparse(url).netloc == self.domain

    def crawl(self):
        print(f"Starting crawl at {self.start_url}...")

        while self.queue:
            current_url, depth = self.queue.popleft()

            if depth > self.max_depth:
                continue

            if current_url in self.visited:
                continue

            self.visited.add(current_url)
            html = self.fetch_page(current_url)

            if html:
                links = self.extract_links(html, current_url)
                for link in links:
                    if self.is_same_domain(link) and link not in self.visited:
                        self.queue.append((link, depth + 1))

        print(f"Crawling complete. {len(self.visited)} URLs found.")
        return self.visited

    def save_results(self, filename, urls):
        with open(filename, "w") as file:
            for url in sorted(urls):
                file.write(url + "\n")
        print(f"Results saved to {filename}.")
