from .error import BaseClassError


class Category:
    def __init__(self):
        self._categories = {
            "business": 'business--events'
        }

    @property
    def category(self):
        raise BaseClassError(class_name=self.__class__.__name__, property_name='category')


class BusinessCategory(Category):
    @property
    def category(self) -> str:
        return self._categories.get("business")
