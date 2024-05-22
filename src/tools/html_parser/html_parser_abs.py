from abc import ABC, abstractmethod
import re


class AbsHtmlAnalyzer(ABC):
    @abstractmethod
    def parse_html(self, *args, **kwargs):
        ...

    @classmethod
    def find_match(cls, pattern: re.Pattern, data) -> str | None:
        """Finds a match in the given string by pattern"""
        match_found = pattern.search(data)
        if match_found:
            return match_found.group(1)
        else:
            return None
