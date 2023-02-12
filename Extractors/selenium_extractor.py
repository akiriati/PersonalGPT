from telnetlib import EC
from typing import List

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from Extractors.segments import break_text_into_segments
from constants import Config


class SeleniumExtractor():
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        url = self.get_url()
        html = self.scrap_from_url(url)
        text = self.extract_from_html(html)
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
        print(url)
        # specify the path to your Chrome profile
        profile = webdriver.ChromeOptions()
        profile.add_argument("user-data-dir="+Config.CHROME_PROFILE)

        # enable headlefss mode
        profile.add_argument("--headless")

        # initialize the browser object
        browser = webdriver.Chrome(options=profile)

        # navigate to the URL of the website you want to extract text from
        browser.get(url)
        html = browser.page_source

        page_text = html

        # close the browser
        browser.close()
        return page_text

    def extract_from_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

