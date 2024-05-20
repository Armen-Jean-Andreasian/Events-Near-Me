import requests


class UrlScraper:
    @staticmethod
    def make_request(url: str, headers: dict = None) -> str:
        """Returns website HTML in string"""
        response = requests.get(url, headers=headers)
        status_code = response.status_code

        if status_code == 429:
            print("Failed: Too Many Requests")
            print("Consider adding/updating the headers and cookies to request")
            exit()
        elif status_code == 404:
            print(
                "Server detected the scrapper and returned 404 status code. Consider adding/updating the headers and cookies to request")
            exit()
        else:
            print(status_code)
            return response.content.decode('unicode_escape')
