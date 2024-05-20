class Category:
    def __init__(self):
        self._categories = {
            "business": 'business--events'
        }

    @property
    def business(self):
        return self._categories.get("business")