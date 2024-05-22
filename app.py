from src.tools.url_scraper.url_params import *
from src.tools.helpers import save_file, save_json_file
from src.web_source_one import SourceOneHtmlAnalyzer, SourceOneScrapHTML, SourceOneJsonAnalyzer
from config import Config


class EventsApp:
    def __init__(self, dotenv_path: str = ".env"):
        self.dotenv_path = dotenv_path
        self.config = Config()

    def get_source_one_html(
            self,
            location: Location,
            entrance_fee: PaidEntrance | FreeEntrance,
            event_category: BusinessCategory | None,
            custom_event_name: str,
            fixed_date: FixedDate,
            custom_date: CustomDate
    ):

        source_one_html_scraper = SourceOneScrapHTML(dotenv_path=self.dotenv_path)
        source_one_html_code = source_one_html_scraper.find_events(location=location,
                                                                   entrance_fee=entrance_fee,
                                                                   event_category=event_category,
                                                                   custom_event_name=custom_event_name,
                                                                   fixed_date=fixed_date,
                                                                   custom_date=custom_date)
        return source_one_html_code

    def find_events(
            self,
            location: Location,
            entrance_fee: PaidEntrance | FreeEntrance = None,
            event_category: BusinessCategory = None,
            custom_event_name: str = None,
            fixed_date: Today | Tomorrow | ThisWeekend = None,
            custom_date: CustomDate = None,
            save_raw_html: bool = False
    ):

        source_one_html_code = self.get_source_one_html(
            location=location,
            entrance_fee=entrance_fee,
            event_category=event_category,
            custom_event_name=custom_event_name,
            fixed_date=fixed_date,
            custom_date=custom_date
        )

        if save_raw_html:
            save_file(content=source_one_html_code, path=self.config.raw_html_file_name)
            print(f"HTML content was saved to {self.config.raw_html_file_name} successfully")

        react_query_json = SourceOneHtmlAnalyzer.parse_html(html_code=source_one_html_code)

        list_of_events: list[dict] = SourceOneJsonAnalyzer.parse_react_query_state(
            react_query_json=react_query_json)

        save_json_file(content=list_of_events, path=self.config.react_query_json_filename)
        print(f"Jsons were saved to {self.config.react_query_json_file_name} ")


if __name__ == "__main__":
    location = Location("Vietnam")
    entrance_fee = PaidEntrance()
    event_category = BusinessCategory()
    event_name = "Pool Party"
    fixed_date = Tomorrow()

    custom_date_start = YYYYMMDDDate(year=2024, month=6, date=7).date
    custom_date_end = YYYYMMDDDate(year=2025, month=1, date=5).date
    custom_date = CustomDate(start_date=custom_date_start, end_date=custom_date_end)

    save_raw_html = False

    events_app = EventsApp()
    events_app.find_events(
        location=location,
        entrance_fee=entrance_fee,
        event_category=event_category,
        custom_event_name=event_name,
        fixed_date=fixed_date,
        custom_date=custom_date,
        save_raw_html=save_raw_html)
