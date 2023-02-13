import requests

from Extractors.Scrappers.scrapper import Scrapper


class RequestsScrapper(Scrapper):

    def get_html(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            content = response.content
            html = content.decode("utf-8")
            return html
        else:
            print("Failed to retrieve content. Response code:", response.status_code)
            return ""





