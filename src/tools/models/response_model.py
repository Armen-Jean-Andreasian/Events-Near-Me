from pydantic import BaseModel, field_validator
from typing import Any, Literal


class ResponseModel(BaseModel):
    status_code: int

    @field_validator('status_code')
    def validate_status_code(cls, code):
        if code not in range(100, 501):
            raise ValueError('status_code must be between 100 and 500')
        return code

    status: Literal["success", "fail", "error"]
    description: str | None = None  # "Task not found"
    data: Any | None = None
    message: str | None = None  # "Consider creating a task"
