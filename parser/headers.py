class RequestHeaders:
    def __init__(self, cookie: str):
        self._headers = {
            'Accept-Encoding': 'gzip, deflate, zstd',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
        }

    @property
    def headers(self):
        return self._headers
