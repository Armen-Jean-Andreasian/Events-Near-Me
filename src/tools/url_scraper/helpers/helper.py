from src.tools.models.response_model import ResponseModel
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    import httpx
    import requests


def return_scrapped_content(response: Union["httpx.Response", "requests.Response"]) -> ResponseModel:
    status_code: int = response.status_code

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
    else:
        try:
            html_code: str = response.content.decode('unicode_escape')
            print('html FOUND:', html_code)
        except Exception as error:
            return ResponseModel(
                status="fail",
                status_code=status_code,
                message=str(error)
            )
        else:
            return ResponseModel(
                status="success",
                status_code=status_code,
                data=html_code
            )
