from .error import BaseClassError


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
    def when(self):
        raise BaseClassError(class_name=self.__class__.__name__, property_name='when')


class Today(FixedDate):
    @property
    def when(self) -> str:
        return self._dates['today']

    def __str__(self):
        return "Today"


class Tomorrow(FixedDate):
    @property
    def when(self) -> str:
        return self._dates['tomorrow']

    def __str__(self):
        return "Tomorrow"


class ThisWeekend(FixedDate):
    @property
    def when(self) -> str:
        return self._dates['this-weekend']

    def __str__(self):
        return "This Weekend"
