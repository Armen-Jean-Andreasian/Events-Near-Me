import asyncio
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from src.tools.url_scraper.get_url_sync import UrlScraperSync
from src.tools.url_scraper.get_url_async import UrlScraperAsync
from src.tools.url_scraper import RequestHeaders
from src.tools.url_scraper.url_params import *

if TYPE_CHECKING:
    from src.tools.models import ResponseModel


class SourceOneHtmlScraperAbs(ABC):
    def __init__(self, cookies: dict, api_base_url: str):
        self.api_base_url = api_base_url
        self.request_headers = RequestHeaders(cookies=cookies).headers

    def _generate_url(self,
                      location: Location,
                      entrance_fee: EntranceFee = None,
                      event_category: Category = None,
                      custom_event_name: str = None,
                      fixed_date: FixedDate = None,
                      custom_date: CustomDate = None) -> str:

        url_generator_obj = UrlGenerator(base_url=self.api_base_url,
                                         location=location,
                                         entrance_fee=entrance_fee,
                                         event_category=event_category,
                                         custom_event_name=custom_event_name,
                                         fixed_date=fixed_date,
                                         custom_date=custom_date)
        return url_generator_obj.url

    @abstractmethod
    def find_events(self,
                    location: Location,
                    entrance_fee: EntranceFee,
                    event_category: Category,
                    custom_event_name: str,
                    fixed_date: FixedDate,
                    custom_date: CustomDate) -> "ResponseModel":
        ...


class SourceOneHtmlScraperSync(SourceOneHtmlScraperAbs):
    def find_events(self,
                    location,
                    entrance_fee=None,
                    event_category=None,
                    custom_event_name=None,
                    fixed_date=None,
                    custom_date=None
                    ):

        url: str = self._generate_url(location=location,
                                      entrance_fee=entrance_fee,
                                      event_category=event_category,
                                      custom_event_name=custom_event_name,
                                      fixed_date=fixed_date,
                                      custom_date=custom_date)

        print(url)
        return UrlScraperSync.make_request(url=url, headers=self.request_headers)


class SourceOneHtmlScraperAsync(SourceOneHtmlScraperAbs):
    async def _make_request(self, url: str):
        return await UrlScraperAsync.make_request(url=url, headers=self.request_headers)

    def find_events(self,
                    location,
                    entrance_fee=None,
                    event_category=None,
                    custom_event_name=None,
                    fixed_date=None,
                    custom_date=None):

        url: str = self._generate_url(location=location,
                                      entrance_fee=entrance_fee,
                                      event_category=event_category,
                                      custom_event_name=custom_event_name,
                                      fixed_date=fixed_date,
                                      custom_date=custom_date)

        print(url)
        return asyncio.run(self._make_request(url=url))
