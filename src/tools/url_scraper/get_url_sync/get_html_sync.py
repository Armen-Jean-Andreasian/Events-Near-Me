import requests
from src.tools.models.response_model import ResponseModel


class UrlScraperSync:
    @staticmethod
    def make_request(url: str, headers: dict = None) -> ResponseModel:
        """Returns website HTML in string"""
        response = requests.get(url, headers=headers)
        status_code = response.status_code

        if status_code == 429:
            return ResponseModel(
                status="fail",
                status_code=status_code,
                message="Server detected the scrapper. Consider adding/updating the headers and cookies to request",
                description="Failed: Too Many Requests"
            )

        elif status_code == 404:
            return ResponseModel(
                status="fail",
                status_code=status_code,
                message="Server returned 404 status code. Data not found on provided query.",
                description="Not found"
            )

        elif status_code == 200:
            html_code: str = response.content.decode('unicode_escape')

            return ResponseModel(
                status="success",
                status_code=status_code,
                data=html_code
            )
