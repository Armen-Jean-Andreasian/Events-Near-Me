from typing import Any, Literal, Optional
from copy import deepcopy


# noinspection PyTypedDict
class ResponseSchema:

    _default_response = {
        "status": None,  # "error"
        "status_code": None,  # 200, 400
        "description": None,  # "Task not found"
        "data": None,
        "message": None
    }

    success = "success"
    fail = "fail"
    error = "error"

    _supported_statuses = (success, fail, error)
    _supported_status_codes = range(100, 600)

    @classmethod
    def generate_response(
            cls,
            status: Literal["success", "fail", "error"],
            status_code: int = None,
            data: Optional[Any] = None,
            message: str = None,
            description: str = None
    ):

        if status not in cls._supported_statuses:
            raise ValueError(f"Invalid status: {status}. Supported statuses {cls._supported_statuses}")

        if status_code and status_code not in cls._supported_status_codes:
            raise ValueError(
                f"Invalid status code: {status_code}. Supported status codes {cls._supported_status_codes}")

        resp_body = deepcopy(cls._default_response)

        resp_body['status'] = status
        resp_body['status_code'] = status_code

        if data is not None:
            resp_body['data'] = data

        if description is not None:
            resp_body['description'] = description

        if message is not None:
            resp_body['message'] = message

        return resp_body
