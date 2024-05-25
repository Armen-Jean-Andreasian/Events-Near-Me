from src.tools.url_scraper.helpers import return_scrapped_content
import httpx, ssl, certifi




class UrlScraperAsync:
	@staticmethod
	async def make_request(url: str, headers: dict = None):
		"""Asynchronously scraps website's HTML code"""
		context = ssl.create_default_context()
		context.load_verify_locations(certifi.where())
		client = httpx.AsyncClient(verify=context)

		async with client:
			response: httpx.Response = await client.get(url, headers=headers, timeout=120)
			return return_scrapped_content(response=response)
