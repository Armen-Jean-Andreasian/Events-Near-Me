from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from src.tools.url_scraper.url_params import *


class UrlGenerator:
    def __init__(
            self,
            base_url: str,
            location: "Location",
            entrance_fee: Union["EntranceFee", None],
            event_category: Union["Category", None],
            custom_event_name: str | None,
            fixed_date: Union["FixedDate", None],
            custom_date: Union["CustomDate", None]
    ):

        url_body = ""

        # base_url/location/body/custom_event_name--fixed_date/?page=1

        if location:
            # https://www.eventbrite.com/d/vietnam/
            str_location: str = location.location
            base_url += f"{str_location}/"

        if entrance_fee:
            # https://www.eventbrite.com/d/vietnam/free/?page=1
            str_entrance_fee: str = entrance_fee.fee
            url_body += str_entrance_fee

        if event_category:
            # https://www.eventbrite.com/d/vietnam/free--business--events/?page=1
            str_category: str = event_category.category
            url_body += f"{str_category}"

        if fixed_date:
            # https://www.eventbrite.com/d/vietnam/free--business--events--today/?page=1
            str_fixed_date: str = fixed_date.when
            url_body += f"{str_fixed_date}"

        if custom_event_name:
            # https://www.eventbrite.com/d/vietnam/free--business--events--today/party/?page=1#search

            stripped_lowercase = '-'.join([word.lower() for word in custom_event_name.split()])

            url_body += f"/{stripped_lowercase}/"

        url_body += '?page=1'  # adding ending

        if custom_date:
            # https://www.eventbrite.com/d/vietnam/business--events--today/party/?page=1&start_date=2024-05-20&end_date=2024-06-13
            str_custom_date: str = custom_date.date
            url_body += str_custom_date

        self.url = base_url + url_body

    @property
    def get_url(self):
        return self.url
