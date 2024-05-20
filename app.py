from src.tools.url_scraper.url_params import (
    UrlGenerator,
    Category,
)
from src.tools.helpers import save_file
from src.tools.helpers import retrieve_dotenv
from src.tools.url_scraper.get_url_sync import UrlScraperSync
from src.tools.url_scraper.request_headers import RequestHeaders
from src.source_one import SourceOneHtmlAnalyzer


class EventsApp:
    def __init__(self, dotenv_path: str, server_data_json_filename: str = None, react_query_json_filename: str = None):

        self.api_base_url = retrieve_dotenv(key="SOURCE_ONE_URL", dotenv_path=dotenv_path)
        self.headers = RequestHeaders(cookie=retrieve_dotenv(key="SOURCE_ONE_COOKIE", dotenv_path=dotenv_path)).headers

        self.server_data_json_filename = server_data_json_filename
        self.react_query_json_filename = react_query_json_filename

    def find_events(self,
                    location: str,
                    entrance_fee: str = None,
                    event_category: str = None,
                    custom_event_name: str = None,
                    fixed_date: str = None,
                    custom_date: str = None,
                    save_raw_html: bool = False,
                    raw_html_filename: str = "results/raw_html.html",
                    server_data_json_filename: str = "results/server-data.json",
                    react_query_json_filename: str = "results/react-query-state.json"):
        url_generator_obj = UrlGenerator(base_url=self.api_base_url,
                                         location=location,
                                         entrance_fee=entrance_fee,
                                         category=event_category,
                                         custom_event_name=custom_event_name,
                                         fixed_date=fixed_date,
                                         custom_date=custom_date)

        url = url_generator_obj.url
        html_code = UrlScraperSync.make_request(url=url, headers=self.headers)

        if save_raw_html:
            save_file(content=html_code, path=raw_html_filename)
            print(f"Content was saved to {raw_html_filename} successfully")

        SourceOneHtmlAnalyzer.parse_html(html_code=html_code,
                                         server_data_json_filename=server_data_json_filename,
                                         react_query_json_filename=react_query_json_filename)


if __name__ == "__main__":
    events_app = EventsApp(dotenv_path=".env")
    events_app.find_events(location="Vietnam",
                           # entrance_fee=EntranceFee().paid,
                           event_category=Category().business,
                           # custom_event_name="Pool          Party          ",
                           # fixed_date=FixedDate().tomorrow,
                           # custom_date=CustomDate.custom_date(
                           #    start_date=YYYYMMDDDate(year=2024, month=6, date=7).date,
                           #    end_date=YYYYMMDDDate(year=2025, month=1, date=5).date)
                           )
