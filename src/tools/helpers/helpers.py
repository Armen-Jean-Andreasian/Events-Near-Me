import dotenv
import json


def retrieve_dotenv(key: str, dotenv_path: str):
    return dotenv.dotenv_values(dotenv_path=dotenv_path).get(key)


def save_file(content: str, path: str):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)


def save_json_file(content: dict, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, indent=4)


def read_json_file(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def str_to_json(json_str_data: str) -> dict:
    """Tries to perform json.loads the sting and return a dict.
    If fails prints details on the char failed the serialization"""

    def print_error_location(json_string, error_position):
        start_index = max(0, error_position - 30)
        end_index = min(len(json_string), error_position + 30)
        problematic_substring = json_string[start_index:end_index]
        print("Problematic substring:", problematic_substring)

    try:
        json_data = json.loads(json_str_data)
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print_error_location(json_str_data, e.pos)
    else:
        return json_data
