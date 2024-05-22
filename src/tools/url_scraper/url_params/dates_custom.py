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

    def __init__(self, start_date: YYYYMMDDDate, end_date: YYYYMMDDDate):
        self._start_date = start_date
        self._end_date = end_date

    @property
    def date(self):
        return self.params.format(start_date=self._start_date, end_date=self._end_date)
