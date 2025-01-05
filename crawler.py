# Main script to execute the crawler

class Crawler:
    def __init__(self, url):
        self.url = url
        
def main():
    url = input("Enter the URL to crawl: ").strip()
    crawler = Crawler(url)
    
    # Start the crawling process
    crawler.crawl()

if __name__ == "__main__":
    main()