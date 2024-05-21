from src.tools.url_scraper.url_params import *
from src.tools.helpers import save_file, save_json_file
from src.web_source_one import SourceOneHtmlAnalyzer, SourceOneScrapHTML
from config import Config
import asyncio


class EventsApp:
    def __init__(self, dotenv_path: str):
        self.dotenv_path = dotenv_path
        self.config = Config()

    def find_events(self,
                    location: str,
                    entrance_fee: str = None,
                    event_category: str = None,
                    custom_event_name: str = None,
                    fixed_date: str = None,
                    custom_date: str = None,
                    save_raw_html: bool = False):

        source_one_html_scraper = SourceOneScrapHTML(dotenv_path=self.dotenv_path)
        source_one_html_code = source_one_html_scraper.find_events(location=location,
                                                                   entrance_fee=entrance_fee,
                                                                   event_category=event_category,
                                                                   custom_event_name=custom_event_name,
                                                                   fixed_date=fixed_date,
                                                                   custom_date=custom_date)

        server_data_json, react_query_json = SourceOneHtmlAnalyzer.parse_html(html_code=source_one_html_code)
        asyncio.run(self._save_jsons(server_data_json, react_query_json))

        if save_raw_html:
            self._save_raw_html(html_content=source_one_html_code)



    def _save_raw_html(self, html_content: str):
        asyncio.run(save_file(content=html_content, path=self.config.raw_html_file_name))
        print(f"HTML content was saved to {self.config.raw_html_file_name} successfully")

    async def _save_jsons(self, server_data_json: dict, react_query_json: dict, html_content: str = None):
        await asyncio.gather(
            save_json_file(content=server_data_json, path=self.config.server_data_json_filename),
            save_json_file(content=react_query_json, path=self.config.react_query_json_file_name)
        )
        print(f"Jsons were saved to {self.config.react_query_json_file_name} and "
              f"{self.config.server_data_json_filename}")


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
                           save_raw_html=True
                           )
