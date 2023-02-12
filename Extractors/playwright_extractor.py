import re
import os
from typing import List

from playwright.sync_api import sync_playwright

from Extractors.segments import break_text_into_segments
from constants import Config


class PlaywrightExtractor():
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        url = self.get_url()
        text = self.scrap_from_url(url)
        return break_text_into_segments(text)

    def get_url(self):
        with open(self.full_filepath, 'r') as file:
            file_contents = file.read()
        url_match = re.search(r'(https?://[^\s]+)', file_contents)
        if url_match:
            return url_match.group(0)
        else:
            raise ValueError(f'URL not found in {self.full_filepath}')

    def scrap_from_url(self, url):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(userDataDir=Config.CHROME_PROFILE)
            page = browser.newPage()
            page.goto(url)
            text_content = page.evaluate("document.body.textContent")
            browser.close()
            return text_content


