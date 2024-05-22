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


class Tomorrow(FixedDate):
    @property
    def when(self) -> str:
        return self._dates['tomorrow']


class ThisWeekend(FixedDate):
    @property
    def when(self) -> str:
        return self._dates['this-weekend']
