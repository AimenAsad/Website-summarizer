#website scraping logic

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No Title"
        for tag in soup(["script", "style", "img", "input"]):
            tag.decompose()
        self.text = soup.get_text(separator="\n", strip=True)

    def get_cleaned_text(self):
        return f"WebPage Title:\n{self.title}\n\nWebPage Contents:\n{self.text[:4000]}"

