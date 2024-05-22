class Location:
    def __init__(self, location: str):
        self._location = self._format(location)

    def _format(self, location):
        stripped_lowercase = '-'.join([word.lower() for word in location.split()])
        return stripped_lowercase

    @property
    def location(self):
        return self._location
