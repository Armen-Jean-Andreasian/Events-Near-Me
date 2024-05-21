import dotenv
import aiofiles
import json


async def save_file(content: str, path: str):
    async with aiofiles.open(path, 'w', encoding='utf-8') as file:
        await file.write(content)


async def save_json_file(content: dict, path: str) -> None:
    async with aiofiles.open(path, 'w', encoding='utf-8') as json_file:
        await json_file.write(json.dumps(content, indent=4))


def retrieve_dotenv(key: str, dotenv_path: str):
    return dotenv.dotenv_values(dotenv_path=dotenv_path).get(key)


def str_to_json(json_str_data: str) -> dict:
    """Tries to perform json.loads the sting and return a dict.
    If fails prints details on the char failed the serialization"""

    def print_error_location(json_string, error_position):
        start_index = max(0, error_position - 10)
        end_index = min(len(json_string), error_position + 10)
        problematic_substring = json_string[start_index:end_index]
        print("Problematic substring:", problematic_substring)

    try:
        json_data = json.loads(json_str_data)
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print_error_location(json_str_data, e.pos)
    else:
        return json_data
