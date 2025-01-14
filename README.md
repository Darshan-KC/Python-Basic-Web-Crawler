
# 🕸️ Python Basic Web Crawler

## 📖 Overview
The **Python Basic Web Crawler** is an educational project that demonstrates how to crawl websites and gather all URLs within a specific domain using Python. This project covers essential concepts such as making HTTP requests, parsing HTML content, and adhering to domain constraints, all implemented using Object-Oriented Programming (OOP) principles.

---

## ✨ Features
- 🌐 **Domain-Specific Crawling**: Collects all internal links within the specified domain.
- ⚡ **Depth Control**: Limits the crawling depth to prevent excessive server load.
- 🛡️ **External Domain Prevention**: Ensures that only links within the target domain are crawled.
- 💾 **Result Storage**: Saves the list of discovered URLs to a text file for further analysis.

---

## 🗂️ Folder Structure
```
Python-Basic-Web-Crawler/
├── venv/                     # Virtual environment (optional)
├── crawler.py                # Main script to initiate the crawling process
├── utils.py                  # Contains the WebCrawler class and helper functions
├── requirements.txt          # List of required Python libraries
├── crawled_urls.txt          # Output file containing the crawled URLs
├── README.md                 # Project documentation
└── .gitignore                # Specifies files to be ignored by Git
```

---

## 🛠️ Setup Instructions
### Prerequisites
- 🐍 **Python**: Version 3.6 or higher
- 📦 **pip**: Python package installer

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Darshan-KC/Python-Basic-Web-Crawler.git
   cd Python-Basic-Web-Crawler
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   # Activate the virtual environment:
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage
1. **Configure the Crawler**:
   - Open `crawler.py`.
   - Modify the `start_url` variable to the desired starting point.
   - Adjust the `max_depth` variable to set the crawling depth limit.

2. **Run the Crawler**:
   ```bash
   python crawler.py
   ```

3. **View Results**:
   - After execution, the crawled URLs will be saved in `crawled_urls.txt`.

---

## 📄 Example Output
Sample entries in `crawled_urls.txt`:
```
https://example.com
https://example.com/about
https://example.com/contact
```

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🔮 Future Enhancements
- 🧵 **Multithreading**: Implement concurrent crawling to improve efficiency.
- ⏱️ **Rate Limiting**: Introduce delays between requests to respect server load.
- 📊 **Data Storage**: Expand support for saving results in formats like JSON or databases.

---

## 📧 Contact
For any inquiries or feedback, please contact [Darshan KC](https://github.com/Darshan-KC).
