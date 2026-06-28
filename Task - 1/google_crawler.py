import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin, urlparse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HackvedaBot/1.0)"
}

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawl_for_marketing(seed_url, keyword, max_links=15):
    results = []

    try:
        response = requests.get(seed_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("Connection error:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.find_all("a", href=True):
        link = urljoin(seed_url, tag["href"])

        if not is_valid_url(link):
            continue

        try:
            page = requests.get(link, headers=HEADERS, timeout=5)
            page_soup = BeautifulSoup(page.text, "html.parser")

            title = page_soup.title.text.strip() if page_soup.title else "No Title"
            description = ""

            meta = page_soup.find("meta", attrs={"name": "description"})
            if meta:
                description = meta.get("content", "")

            if keyword.lower() in (title + description).lower():
                results.append([link, title, description])

            if len(results) >= max_links:
                break

        except:
            continue

    save_to_csv(results)

def save_to_csv(data):
    with open("marketing_leads.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Title", "Meta Description"])
        writer.writerows(data)

    print("✔ Marketing data saved to marketing_leads.csv")

# DEMO RUN
crawl_for_marketing(
    seed_url="https://www.python.org",
    keyword="python",
    max_links=10
)


