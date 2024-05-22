class SourceOneJsonAnalyzer:
    @staticmethod
    def parse_react_query_state(react_query_json: dict) -> list[dict[str, str]]:
        # brutal, dry and uncensored data science magic below. gonna hurt Martin's principles

        results: list[dict] = react_query_json["queries"][0]["state"]["data"]["events"]["results"]

        react_query_state_results = []
        temp = {}
        try:
            for event_details_dict in results:
                temp["image"]: str = event_details_dict.get("image").get("original").get("url")

                temp["is_online_event"]: bool = event_details_dict.get("is_online_event")
                temp["name"]: str = event_details_dict.get("name")

                primary_venue: dict = event_details_dict.get("primary_venue")
                temp["venue_name"]: str = primary_venue.get("name")
                temp["address_1"]: str = primary_venue.get("address_1")
                temp["address_2"]: str = primary_venue.get("address_2")
                temp["city"]: str = primary_venue.get("city")
                temp["region"]: str = primary_venue.get("region")
                temp["country"]: str = primary_venue.get("country")
                temp["latitude"]: str = primary_venue.get("latitude")
                temp["longitude"]: str = primary_venue.get("longitude")
                temp["postal_code"]: str = primary_venue.get("postal_code")

                temp["start_date"]: str = event_details_dict.get("start_date")
                temp["start_time"]: str = event_details_dict.get("start_time")
                temp["summary"]: str = event_details_dict.get("summary")

                react_query_state_results.append(temp.copy())  # python is linkedin crap that's why .copy()
                temp.clear()

        except KeyError:
            # It Was At This Moment We Knew... We ****ed Up
            raise Exception("If you see this for the first time, it may mean that no events found."
                            "If not the Json structure of react_query_json has been changed.")


        return react_query_state_results
