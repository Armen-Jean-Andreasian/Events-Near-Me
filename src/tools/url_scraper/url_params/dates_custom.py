from src.tools.helpers import TestingSkillIssueError


class YYYYMMDDDate:
    def __init__(self, year: int, month: int, date: int):
        self._date = f"{year}-{month}-{date}"

    @property
    def date(self) -> str:
        return self._date


class CustomDate:
    """
    Adds to the end of the link
        https://www.eventbrite.com/d/vietnam/business--events/party/?page=1&start_date=2024-05-20&end_date=2024-06-13
    """

    def __new__(cls, *args, **kwargs):
        cls.params: str = "&start_date={start_date}&end_date={end_date}"
        return super().__new__(cls)

    def __init__(self, start_date: YYYYMMDDDate | str, end_date: YYYYMMDDDate | str):
        """
        :param start_date: `YYYYMMDDDate` instance, or `str` and only in YYYY-MM-DD format
        :param end_date:  `YYYYMMDDDate` instance, or `str` and only in YYYY-MM-DD format

        Both params should be the same type, whether YYYYMMDDDate or str!

        """
        if isinstance(start_date, YYYYMMDDDate) and isinstance(end_date, YYYYMMDDDate):
            self._start_date = start_date.date
            self._end_date = end_date.date

        elif isinstance(start_date, str) and isinstance(end_date, str):
            if len(start_date.split('-')) and len(end_date.split('-')) != 3:
                raise TestingSkillIssueError(
                    "Wrong format! str type dates should correspond YYYY-MM-DD format"
                    "Please read the docstring."
                )

            self._start_date = start_date
            self._end_date = end_date

        else:
            if not type(start_date) is type(end_date):
                raise TestingSkillIssueError(
                    "You were informed to not pass different types for start_date and end_date!"
                    "Please read the docstring."
                )


    @property
    def date(self):
        return self.params.format(start_date=self._start_date, end_date=self._end_date)
