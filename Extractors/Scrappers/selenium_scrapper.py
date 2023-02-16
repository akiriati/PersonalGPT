
from selenium import webdriver

from bs4 import BeautifulSoup

from constants import Config

class PlaywrightScrapper():

    def get_html(self, url):

        # specify the path to your Chrome profile
        profile = webdriver.ChromeOptions()
        profile.add_argument()

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

