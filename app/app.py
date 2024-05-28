from config import Config
from src.tools.url_scraper.url_params import *
from src.tools.helpers import save_file
from src.tools.helpers import save_json_file
from src.web_source_one import SourceOneHtmlAnalyzer
from src.web_source_one import SourceOneHtmlScraperSync
from src.web_source_one import SourceOneHtmlScraperAsync
from src.web_source_one import SourceOneJsonParser
# from src.web_source_one import SourceOneJsonParserWithoutCustomEvent
from src.tools.models.response_model import ResponseModel


class EventsApp:
	def __init__(self, api_base_url: str, cookie: str):
		self.api_base_url = api_base_url
		self.cookie = cookie

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
			# use_react_query_state: bool = False,
	) -> dict | None:

		source_one_html_scraper = SourceOneHtmlScraperAsync(api_base_url=self.api_base_url, cookies=self.cookie)

		scraper_response: ResponseModel = source_one_html_scraper.find_events(
			location, entrance_fee, event_category, custom_event_name, fixed_date, custom_date)

		source_one_html_code: str = scraper_response.data

		if save_raw_html:
			save_file(content=source_one_html_code, path=Config.raw_html_filename)
			print(f"HTML content was saved to {Config.raw_html_filename} successfully")

		if scraper_response.status != "success":
			print(scraper_response.model_dump())
			exit()
		else:
			html_analyzer = SourceOneHtmlAnalyzer(html_source=source_one_html_code)
			clear_html: str = html_analyzer.parse_html()

			jsons_found: dict[dict] = html_analyzer.extract_json_from_html(
				json_str=clear_html,
				use_server_data=use_server_data,
				# use_react_query_state=use_react_query_state
			)

			if save_clear_html:
				save_file(content=clear_html, path=Config.clear_html_filename)

			server_data = jsons_found.get(Config.server_data_dict_key)

			save_json_file(content=server_data, path=Config.server_data_json_filepath)
			print(f"Json was saved to {Config.server_data_json_filepath} ")

			result = SourceOneJsonParser.parse_server_data(server_data)

			# if use_react_query_state:
			#     react_query_state = data_dict.get(Config.react_query_dict_key)
			#     self.save_json(content=react_query_state, path=Config.react_query_json_filepath)

			return ResponseModel(
				status="success",
				status_code=200,
				data=result
			)
