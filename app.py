from src.tools.url_scraper.url_params import *
from src.tools.helpers import save_file, save_json_file
from src.web_source_one import SourceOneHtmlAnalyzer, SourceOneScrapHTML
from src.tools.helpers import retrieve_dotenv
from config import Config


class EventsApp:
    dotenv_url_key = "SOURCE_ONE_URL"
    dotenv_cookies_key = "SOURCE_ONE_COOKIE"

    def __init__(self, dotenv_path: str = ".env"):
        self.api_base_url = retrieve_dotenv(key=self.dotenv_url_key, dotenv_path=dotenv_path)
        self.__cookies = retrieve_dotenv(key=self.dotenv_cookies_key, dotenv_path=dotenv_path)

    def get_source_one_html(
            self,
            location: Location,
            entrance_fee: PaidEntrance | FreeEntrance,
            event_category: BusinessCategory | None,
            custom_event_name: str,
            fixed_date: FixedDate,
            custom_date: CustomDate
    ):
        source_one_html_scraper = SourceOneScrapHTML(api_base_url=self.api_base_url, cookies=self.__cookies)
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
            save_raw_html: bool = False,
            save_clear_html: bool = False,
            use_server_data: bool = True,
            use_react_query_state: bool = False,
    ):
        source_one_html_code = self.get_source_one_html(
            location, entrance_fee, event_category, custom_event_name, fixed_date, custom_date
        )

        if save_raw_html:
            save_file(content=source_one_html_code, path=Config.raw_html_filename)
            print(f"HTML content was saved to {Config.raw_html_filename} successfully")

        html_analyzer = SourceOneHtmlAnalyzer(html_source=source_one_html_code)
        clear_html = html_analyzer.parse_html()

        if save_clear_html:
            save_file(content=clear_html, path=Config.clear_html_filename)
            print(f"HTML content was saved to {Config.clear_html_filename} successfully")


        jsons_found: dict[dict] = html_analyzer.extract_json_from_html(json_str=clear_html,
                                                                       use_server_data=use_server_data,
                                                                       use_react_query_state=use_react_query_state)

        if use_server_data:
            save_json_file(content=jsons_found.get(Config.server_data_dict_key), path=Config.server_data_json_filepath)
            print(f"Json was saved to {Config.server_data_json_filepath} ")

        elif use_react_query_state:  # the server returns a broken json
            save_json_file(content=jsons_found.get(Config.react_query_dict_key), path=Config.react_query_json_filename)
            print(f"Json was saved to {Config.react_query_json_filename} ")

        # done


if __name__ == "__main__":
    location = Location("Colombia")
    entrance_fee = PaidEntrance()
    event_category = BusinessCategory()
    event_name = "Pool Party"
    fixed_date = Tomorrow()

    custom_date_start = YYYYMMDDDate(year=2024, month=6, date=7).date
    custom_date_end = YYYYMMDDDate(year=2025, month=1, date=5).date
    custom_date = CustomDate(start_date=custom_date_start, end_date=custom_date_end)

    save_raw_html = True
    save_clear_html = True

    use_server_data = True
    use_react_query_state = True

    events_app = EventsApp()
    events_app.find_events(
        location=location,
        entrance_fee=entrance_fee,
        event_category=event_category,
        custom_event_name=event_name,
        fixed_date=fixed_date,
        custom_date=custom_date,
        save_raw_html=save_raw_html,
        save_clear_html=save_clear_html,
        use_server_data=use_server_data,
        use_react_query_state=use_react_query_state
    )
