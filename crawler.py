# Main script to execute the crawler

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
    
    def __init__(self, url):
        """
        Initializes the Crawler object with the specified URL.

        Parameters:
        -----------
        url : str
            The URL of the website to be crawled.
        """
        self.url = url
        
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
        
        
def main():
    url = input("Enter the URL to crawl: ").strip()
    crawler = Crawler(url)
    
    # Start the crawling process
    crawler.crawl()

if __name__ == "__main__":
    main()