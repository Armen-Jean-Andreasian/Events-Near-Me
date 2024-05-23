class SourceOneJsonParser:
    @staticmethod
    def parse_server_data(server_data: dict) -> list[dict] | None:
        """Analyzes the data and returns a list of events data packed in dictionaries"""

        events = server_data.get('search_data').get('events')
        num_events = events.get('pagination').get('object_count')

        if int(num_events) == 0:
            print('no events found')

        else:
            events_found = events.get('results')
            server_data_results = []
            temp = {}
            try:
                for event_details_dict in events_found:
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

                    server_data_results.append(temp.copy())  # python is linkedin crap that's why .copy()
                    temp.clear()
            except KeyError:
                # It Was At This Moment We Knew... We ****ed Up
                raise Exception("If you see this for the first time, it may mean that no events found."
                                "If not the Json structure of server_data has been changed.")

            else:
                return server_data_results
