import re
from src.tools.helpers import str_to_json
from src.tools.html_parser import AbsHtmlAnalyzer


class SourceOneHtmlAnalyzer(AbsHtmlAnalyzer):
    @classmethod
    def parse_html(cls, html_code: str) -> tuple[dict, dict]:
        """
        Scraps the url and gets the HTML code,
        Removes the HTML-specific leftover symbols,
        Extracts the json data out of HTML code, checks if it's broken and fixes,
        Saves them to two json files
        """

        script_html_content: str = cls._detect_script_part(html_code)

        pure_script_content: str = cls._trim_html_tags(script_html_content)

        return cls._extract_json(json_str=pure_script_content)

    @classmethod
    def _detect_script_part(cls, html_code):
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
        script_match = script_pattern.search(html_code)

        if script_match:
            return script_match.group(0)  # Full <script> tag content
        else:
            print("Failed to find the specified <script> tag content in the HTML.")
            exit()

    @classmethod
    def _trim_html_tags(cls, html_code: str) -> str:
        """Removes the unnecessary data from the HTML code containing json data and returns it as string"""
        content = html_code[290:]
        clean_text = re.sub(r'<[^>]+>', '', content)
        clean_text = clean_text.strip()
        clean_text = clean_text.replace('};', '}')
        clean_text = clean_text.replace('window.__SERVER_DATA__', 'SERVER_DATA', 1)
        clean_text = clean_text.replace('window.__REACT_QUERY_STATE__', 'REACT_QUERY_STATE', 1)
        return clean_text

    @classmethod
    def _extract_json(cls, json_str: str) -> tuple[dict, dict]:
        """Extracts the json from the str HTML, fixes the broken parts of it and returns a tuple of two dicts"""
        content = json_str.split('REACT_QUERY_STATE = ')

        server_data_json: str = content[0].split('SERVER_DATA = ')[1].strip()
        react_query_state_json: str = content[1].strip()

        react_query_state_json_issue1 = str('"queryHash":"["')
        react_query_state_json_issue1_fix = str('"queryHash":["')

        react_query_state_json_issue2 = str(']}]"}]}')
        react_query_state_json_issue2_fix = str(']}]}]}')

        if react_query_state_json_issue1 in react_query_state_json:
            react_query_state_json = react_query_state_json.replace(react_query_state_json_issue1,
                                                                    react_query_state_json_issue1_fix)
        if react_query_state_json_issue2 in react_query_state_json:
            react_query_state_json = react_query_state_json.replace(react_query_state_json_issue2,
                                                                    react_query_state_json_issue2_fix)

        return str_to_json(server_data_json), str_to_json(react_query_state_json)
