import os


class Config:
    results_folder = 'results'

    server_data_json_filepath = os.path.join(results_folder, "server_data.json")
    server_data_dict_key = 'server_data'

    react_query_json_filename = os.path.join(results_folder, "react_query_state.json")
    react_query_dict_key = 'react_query_state'

    raw_html_filename = os.path.join(results_folder, "raw.html")
    clear_html_filename = os.path.join(results_folder, "clear.html")
