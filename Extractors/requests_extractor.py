import requests
import re
from typing import List

from bs4 import BeautifulSoup

from Extractors.segments import break_text_into_segments
from constants import Config


class RequestsExtractor():
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        url = self.get_url()
        text = self.scrap_from_url(url)
        return break_text_into_segments(text)

    def get_url(self):
        with open(self.full_filepath, 'r') as file:
            file_contents = file.read()
        url_match = re.search(r'(https?://[^\s"]+)', file_contents)
        if url_match:
            return url_match.group(0)
        else:
            raise ValueError(f'URL not found in {self.full_filepath}')

    def scrap_from_url(self, url):
        response = requests.get(url)
        text_in_page = ""

        if response.status_code == 200:
            content = response.content
            html = content.decode("utf-8")
            soup = BeautifulSoup(html, 'html.parser')
            text_in_page = soup.get_text()
        else:
            print("Failed to retrieve content. Response code:", response.status_code)
        return text_in_page





