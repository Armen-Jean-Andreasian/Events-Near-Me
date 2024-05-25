import requests
from src.tools.url_scraper.helpers import return_scrapped_content


class UrlScraperSync:
    @staticmethod
    def make_request(url: str, headers: dict = None):
        """Scraps website's HTML code"""
        response: requests.Response = requests.get(url, headers=headers)
        return return_scrapped_content(response=response)
