import dotenv


def retrieve_dotenv(key: str, dotenv_path: str):
	return dotenv.dotenv_values(dotenv_path=dotenv_path).get(key)
