from src.tools.helpers import retrieve_dotenv
from src.tools.url_scraper import RequestHeaders
from src.tools.url_scraper.url_params import *
from src.tools.url_scraper.get_url_sync import UrlScraperSync


class SourceOneScrapHTML:
    dotenv_url_key = "SOURCE_ONE_URL"
    dotenv_cookies_key = "SOURCE_ONE_COOKIE"

    def __init__(self, dotenv_path: str):
        self.api_base_url = retrieve_dotenv(key=self.dotenv_url_key, dotenv_path=dotenv_path)

        cookies = retrieve_dotenv(key=self.dotenv_cookies_key, dotenv_path=dotenv_path)
        self.request_headers = RequestHeaders(cookies=cookies).headers

    def find_events(
            self,
            location: Location,
            entrance_fee: EntranceFee = None,
            event_category: Category = None,

            custom_event_name: str = None,
            fixed_date: FixedDate = None,
            custom_date: CustomDate = None
    ):

        url_generator_obj = UrlGenerator(base_url=self.api_base_url,
                                         location=location,
                                         entrance_fee=entrance_fee,
                                         event_category=event_category,
                                         custom_event_name=custom_event_name,
                                         fixed_date=fixed_date,
                                         custom_date=custom_date)

        url = url_generator_obj.url
        print(url)
        html_code = UrlScraperSync.make_request(url=url, headers=self.request_headers)

        return html_code
