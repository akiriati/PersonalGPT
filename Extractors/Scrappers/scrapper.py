
import abc


class Scrapper():
    @abc.abstractmethod
    def get_html(self, url):
        pass