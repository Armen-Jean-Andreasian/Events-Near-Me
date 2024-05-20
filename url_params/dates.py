class FixedDate:
    """
    goes to the middle end

    https://www.eventbrite.com/d/vietnam/business--events--today/party/?page=1
    """
    def __init__(self):
        self._dates = {
            'today': '--today',
            'tomorrow': '--tomorrow',
            'this-weekend': '--this-weekend',
        }

    @property
    def today(self):
        return self._dates['today']

    @property
    def tomorrow(self):
        return self._dates['tomorrow']

    @property
    def this_weekend(self):
        return self._dates['this-weekend']


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

    @staticmethod
    def custom_date(start_date: YYYYMMDDDate, end_date: YYYYMMDDDate):
        params = f"&start_date={start_date}&end_date={end_date}"
        return params
