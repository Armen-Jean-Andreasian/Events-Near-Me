class EntranceFee:
    def __init__(self):
        self._fees = {
            'free': 'free--',
            'paid': 'paid--'
        }

    @property
    def free(self):
        return self._fees.get('free')

    @property
    def paid(self):
        return self._fees.get('paid')
