import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

# ANSI Styles
class Styles:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Validate URL format
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Normalize and clean keywords list
def clean_keywords(raw_keywords):
    return [kw.strip().lower() for kw in raw_keywords if kw.strip()]

# Main Crawler function
def crawl(start_url, keywords, max_pages=50):
    visited_urls = set()
    url_queue = [start_url]
    pages_crawled = 0

    while url_queue and pages_crawled < max_pages:
        url = url_queue.pop(0)
        if url in visited_urls:
            continue
        visited_urls.add(url)

        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            pages_crawled += 1
            print(f"{Styles.CYAN}Crawling:{Styles.RESET} {url}")
        except Exception as e:
            print(f"{Styles.RED}Failed to retrieve {url}: {e}{Styles.RESET}")
            continue

        # Search for keywords in page text
        page_text = soup.get_text().lower()
        for keyword in keywords:
            if keyword in page_text:
                print(f"{Styles.GREEN}Keyword '{keyword}' found at: {url}{Styles.RESET}")

        # Extract and queue new links
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)

            if urlparse(full_url).netloc != urlparse(start_url).netloc:
                continue  # Skip external links

            if is_valid_url(full_url) and full_url not in visited_urls:
                url_queue.append(full_url)

    print(f"\n{Styles.BOLD}Crawling complete!{Styles.RESET}")
    print(f"{Styles.YELLOW}Visited URLs count: {len(visited_urls)}{Styles.RESET}")

    with open("visited_urls.txt", "w") as f:
        for url in visited_urls:
            f.write(url + "\n")
    print(f"{Styles.GREEN}Visited URLs saved to 'visited_urls.txt'{Styles.RESET}")

# Entry point
def main():
    print(f"{Styles.BOLD}{Styles.CYAN}Welcome to the Web Crawler!{Styles.RESET}")
    start_url = input("Enter the URL to crawl: ").strip()
    raw_keywords = input("Enter keywords to search (comma-separated): ").split(',')
    keywords = clean_keywords(raw_keywords)
    crawl(start_url, keywords)

if __name__ == "__main__":
    main()