
import re
from typing import List

from bs4 import BeautifulSoup

from Extractors.Scrappers.scrapper import Scrapper
from Extractors.Segmentors.segmentor import Segmentor


class LinkExtractor():
    def __init__(self, segmentor: Segmentor, scrapper: Scrapper):
        self.segmentor = segmentor
        self.scrapper = scrapper

    def get_segments(self, full_filepath: str) -> List[str]:
        url = self.get_url(full_filepath)
        html = self.scrapper.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        text_in_page = soup.get_text()
        return self.segmentor.break_text_into_segments(text_in_page)

    def get_url(self, full_filepath: str):
        with open(full_filepath, 'r') as file:
            file_contents = file.read()
        url_match = re.search(r'(https?://[^\s"]+)', file_contents)
        if url_match:
            return url_match.group(0)
        else:
            raise ValueError(f'URL not found in {full_filepath}')





