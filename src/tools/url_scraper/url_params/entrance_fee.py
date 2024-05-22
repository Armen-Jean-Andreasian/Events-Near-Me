from .error import BaseClassError


class EntranceFee:
    def __init__(self):
        self._fees = {
            'free': 'free--',
            'paid': 'paid--'
        }

    @property
    def fee(self):
        raise BaseClassError(class_name=self.__class__.__name__, property_name="fee")


class FreeEntrance(EntranceFee):

    @property
    def fee(self):
        return self._fees.get('free')


class PaidEntrance(EntranceFee):
    @property
    def fee(self):
        return self._fees.get('paid')
