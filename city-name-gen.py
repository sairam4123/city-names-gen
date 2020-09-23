import requests
import typing
from pathlib import Path
# response = requests.get("https://www.mithrilandmages.com/utilities/CityNamesServer.php?count=50&dataset=india&_=1599126408513")
# print(response.text)
# print(response.text.replace("<br />", ""))
class InvalidDataSet(Exception):
    pass

def get_city_names(file_name: typing.Optional[typing.Union[Path, str]] = Path("some-city-names.txt"), dataset: str = "india", count: int = 50, **options: typing.Dict[str, typing.Any]) -> typing.Optional[typing.Union[typing.NoReturn, str]]:
    def _request_city_names_from_api():
        with requests.get(f"https://www.mithrilandmages.com/utilities/CityNamesServer.php?count={count}&dataset={dataset}") as response:
            if response.text.startswith("Query failed") or response.status_code != 200:
                raise InvalidDataSet("dataset is invalid")
            return response.text.replace("<br />", "")
    if count > 50:
        raise ValueError("maximum city names you can via get_city_names is 50")
    if not file_name: return _request_city_names_from_api()
    with open(file_name, "a", encoding="utf-8", **options) as city_names_file:
        city_names_file.write(_request_city_names_from_api())

get_city_names(dataset="united_states", count=50)