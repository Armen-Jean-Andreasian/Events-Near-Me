from src.tools.url_scraper import RequestHeaders
from src.tools.url_scraper.url_params import *
from src.tools.url_scraper.get_url_sync import UrlScraperSync
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.tools.models import ResponseModel


class SourceOneScrapHTML:
    def __init__(self, cookies: dict, api_base_url: str):
        self.api_base_url = api_base_url
        self.request_headers = RequestHeaders(cookies=cookies).headers

    def find_events(
            self,
            location: Location,
            entrance_fee: EntranceFee = None,
            event_category: Category = None,

            custom_event_name: str = None,
            fixed_date: FixedDate = None,
            custom_date: CustomDate = None
    ) -> "ResponseModel":

        url_generator_obj = UrlGenerator(base_url=self.api_base_url,
                                         location=location,
                                         entrance_fee=entrance_fee,
                                         event_category=event_category,
                                         custom_event_name=custom_event_name,
                                         fixed_date=fixed_date,
                                         custom_date=custom_date)

        url = url_generator_obj.url
        print(url)
        return UrlScraperSync.make_request(url=url, headers=self.request_headers)
