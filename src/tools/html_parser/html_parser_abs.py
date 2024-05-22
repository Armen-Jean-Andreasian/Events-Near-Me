from abc import ABC, abstractmethod


class AbsHtmlAnalyzer(ABC):
    @abstractmethod
    def parse_html(self, *args, **kwargs):
        ...
