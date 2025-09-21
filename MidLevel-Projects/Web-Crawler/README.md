### Title: Web Crawler

---

### Short Description
- A simple Python-based **Web Crawler** that searches web pages for user-specified keywords.
- The crawler navigates links within the same domain, provides real-time progress updates using ANSI terminal colors, and saves all visited URLs to a file.

---

### Features
- Crawl web pages starting from a specified URL.
- Search for keywords on each page.
- Skip external links to stay within the same domain.
- Limit the number of pages to crawl (**max pages**).
- Save all visited URLs to **visited_urls.txt**.
- ANSI-styled console output for better readability.

---

### Built With
- Python 3
- [`requests`](https://pypi.org/project/requests/) -> for HTTP requests
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) -> for HTML parsing
- [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) -> for URL handling

---

### How to Run
- Install dependencies:
  ```bash
  pip install requests beautifulsoup4
- Run the program:
  ```bash
  python web_crawler.py

---

### License
- This project is licensed under the MIT License.