# Main script to execute the crawler

from utils import WebCrawler

class Crawler:
    """
    A simple web crawler class to scrape content from a given URL.

    Attributes:
    -----------
    url : str
        The URL of the website to be crawled.

    Methods:
    --------
    __init__(url: str):
        Initializes the Crawler object with the given URL.

    crawl():
        Starts the crawling process by fetching the URL and parsing the content.
    """
    
    def __init__(self, url, max_depth):
        """
        Initializes the Crawler object with the specified URL.

        Parameters:
        -----------
        url : str
            The URL of the website to be crawled.
        
        max_depth : int
            Limit crawling depth to avoid overloading servers
        """
        self.url = url
        self.max_depth = max_depth
        
    def crawl(self):
        """
        Initiates the crawling process, fetching the content from the specified URL.
        This method is a placeholder for the actual crawling logic, which can include:
        - Making HTTP requests
        - Parsing HTML content
        - Extracting links or other relevant data
        
        Currently, this function only prints the URL to indicate that crawling has started.
        """
        print(f"Starting crawl on: {self.url}")
        # Placeholder for the actual crawling logic (HTTP request, parsing, etc.)
        # You would typically use requests, BeautifulSoup, etc. to implement the full crawling logic.
        crawler = WebCrawler(self.start_url, self.max_depth)
        crawled_urls = crawler.crawl()

        # Save the results to a file
        crawler.save_results("crawled_urls.txt", crawled_urls)
        
        
def main():
    url = input("Enter the URL to crawl: ").strip()
    
    max_depth = input("Enter the max depth: ")
    
    crawler = Crawler(url,max_depth)
    
    
    # Start the crawling process
    crawler.crawl()

if __name__ == "__main__":
    main()