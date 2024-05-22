import json
import re
from src.tools.html_parser import AbsHtmlAnalyzer
from config import Config


class SourceOneHtmlAnalyzer(AbsHtmlAnalyzer):
    def __init__(self, html_source: str):
        self.html_source = html_source
        self.script_tag_html_raw = None
        self.script_tag_html_pure = None

    def parse_html(self) -> str:
        """
        Detects the block with JSON contents.

        Scraps the url and gets the HTML code,
        Removes the HTML-specific leftover symbols,
        Returns the clear HTML block containing the JSONS
        """

        self.script_tag_html_raw: str = self._detect_script_part(self.html_source)
        self.script_tag_html_pure: str = self._trim_html_leftovers(self.script_tag_html_raw)
        return self.script_tag_html_pure

    @staticmethod
    def _detect_script_part(html_source: str):
        """ As the json is located inside the  script tag, this method detects the content of it."""
        script_pattern = re.compile(
            r'<script type="text/javascript">\s*'
            r'// Get user\'s timezone and save in cookies\s*'
            r'const timezone = Intl.DateTimeFormat\(\).resolvedOptions\(\).timeZone;\s*'
            r'document.cookie = "django_timezone=" \+ timezone;\s*'
            r'window\.__i18n__ = \{.*?\};\s*'
            r'(.*?)'
            r'</script>', re.DOTALL
        )
        script_match = script_pattern.search(html_source)

        if script_match:
            script_tag_html_raw = script_match.group(0)  # Full <script> tag content
            return script_tag_html_raw
        else:
            print("Failed to find the specified <script> tag content in the HTML.")
            exit()

    @staticmethod
    def _trim_html_leftovers(script_tag_html: str) -> str:
        """Removes the unnecessary data from the HTML code containing json data and returns it as string"""
        content = script_tag_html[290:]
        clean_text = re.sub(r'<[^>]+>', '', content)
        clean_text = clean_text.strip()
        clean_text = clean_text.replace('};', '}')
        clean_text = clean_text.replace('window.__SERVER_DATA__', 'SERVER_DATA', 1)
        clean_text = clean_text.replace('window.__REACT_QUERY_STATE__', 'REACT_QUERY_STATE', 1)
        return clean_text

    def extract_json_from_html(
            self,
            json_str: str,
            use_server_data: bool = False,
            use_react_query_state: bool = False
    ) -> dict[dict]:
        """
        Extracts the jsons from the str HTML, fixes the broken parts of it and returns a list of string json objects.
        """
        result = dict()

        if use_server_data:
            server_data_pattern = re.compile(r'SERVER_DATA\s*=\s*(\{.*?\})\s{47}', re.DOTALL)
            server_data_match = server_data_pattern.search(json_str)

            if server_data_match:
                server_data_str = server_data_match.group(1)
                server_data_json = json.loads(server_data_str)
                result[Config.server_data_dict_key] = server_data_json

        if use_react_query_state:
            react_query_state_pattern = re.compile(r'REACT_QUERY_STATE\s*=\s*(\{.*?\})', re.DOTALL)
            react_query_state_match = react_query_state_pattern.search(json_str)

            if react_query_state_match:
                react_query_state_str = self.find_match(pattern=react_query_state_pattern, data=json_str)

                try:
                    react_query_state_json = json.loads(react_query_state_str)
                    result[Config.react_query_dict_key] = react_query_state_json

                except json.decoder.JSONDecodeError as e:
                    print(f"Failed to fetch react query state due to {str(e)}")

        return result

    @property
    def source_code(self):
        return self.html_source

    @property
    def tag_html_raw(self):
        return self.script_tag_html_raw

    @property
    def tag_html_clear(self):
        return self.script_tag_html_pure
