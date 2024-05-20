class UrlGenerator:
    def __init__(self, base_url: str, location: str, entrance_fee, category: str = None, custom_event_name: str = None,
                 fixed_date=None, custom_date=None):

        url_body = ""

        # base_url/location/body/custom_event_name--fixed_date/?page=1

        if location:
            # https://www.eventbrite.com/d/vietnam/
            stripped_lowercase = '-'.join([word.lower() for word in location.split()])

            base_url += f"{stripped_lowercase}/"

        if entrance_fee:
            # https://www.eventbrite.com/d/vietnam/free/?page=1
            url_body += entrance_fee

        if category:
            # https://www.eventbrite.com/d/vietnam/free--business--events/?page=1
            url_body += f"{category}"

        if fixed_date:
            # https://www.eventbrite.com/d/vietnam/free--business--events--today/?page=1
            url_body += f"{fixed_date}"

        if custom_event_name:
            # https://www.eventbrite.com/d/vietnam/free--business--events--today/party/?page=1#search

            stripped_lowercase = '-'.join([word.lower() for word in custom_event_name.split()])

            url_body += f"/{stripped_lowercase}/"

        url_body += '?page=1'  # adding ending

        if custom_date:
            # https://www.eventbrite.com/d/vietnam/business--events--today/party/?page=1&start_date=2024-05-20&end_date=2024-06-13
            url_body += custom_date

        self.url = base_url + url_body

    @property
    def get_url(self):
        return self.url
