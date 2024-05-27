from src.tools.url_scraper.helpers import return_scrapped_content
import httpx
import ssl, certifi


class UrlScraperAsync:
	@staticmethod
	async def make_request(url: str, headers: dict = None, timeout: int = 30):
		"""Asynchronously scraps website's HTML code."""

		# uncomment if certificates will be needed

		# context = ssl.create_default_context()
		# context.load_verify_locations(certifi.where())

		client = httpx.AsyncClient(
			# verify=context,
			follow_redirects=False,
			timeout=timeout,
			headers=headers
		)

		async with client:
			response: httpx.Response = await client.get(url=url)
			while response.status_code in (301, 302, 303, 307, 308):
				destination: str = response.headers.get('location')
				if not destination:
					raise ValueError("Received a response with a redirect status code without destination.")

				response = await client.get(url=destination)
			return return_scrapped_content(response=response)
