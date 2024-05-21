class Config:
    server_data_json_file_name: str = "results/server-data.json"
    react_query_json_file_name: str = "results/react-query-state.json"
    raw_html_file_name: str = "results/raw_html.html"

    @property
    def server_data_json_filename(self):
        return self.server_data_json_file_name

    @property
    def react_query_json_filename(self):
        return self.react_query_json_file_name


    @property
    def raw_html_filename(self):
        return self.raw_html_file_name

