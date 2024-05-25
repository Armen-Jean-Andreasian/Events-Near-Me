def extract_jsonld(server_data: dict):
    jsonld_found: list[dict] = server_data.get('jsonld')
    elements: list[dict] = jsonld_found[0].get('itemListElement')  # list of dicts

    server_data_results = []
    temp = {}

    def search_and_add(container_key: str, source_key: str, container: dict, source: dict):
        if source_key in source:
            container[container_key] = source.get(source_key)
        return container

    for element in elements:
        if 'item' in element:
            item = element.get('item')
            temp = search_and_add(source_key='startDate', container_key='start_date', container=temp, source=item)

            temp = search_and_add(source_key='endDate', container_key='end_date', container=temp, source=item)
            temp = search_and_add(source_key='description', container_key='description', container=temp, source=item)
            temp = search_and_add(source_key='image', container_key='image', container=temp, source=item)
            temp = search_and_add(source_key='name', container_key='name', container=temp, source=item)


            location = item.get("location")

            if location:
                temp = search_and_add(source_key='name', container_key='venue_name', container=temp, source=location)

            address = location.get('address')
            if address:  # some events don't have address

                temp = search_and_add(source_key='addressCountry', container_key='country', container=temp, source=address)
                temp = search_and_add(source_key='addressLocality', container_key='city', container=temp, source=address)
                temp = search_and_add(source_key='addressRegion', container_key='region', container=temp, source=address)
                temp = search_and_add(source_key='postalCode', container_key='postal_code', container=temp, source=address)
                temp = search_and_add(source_key='streetAddress', container_key='address_1', container=temp, source=address)

                geo = location.get('geo')
                if geo:  # just in case
                    temp = search_and_add(source_key='latitude', container_key='latitude', container=temp, source=geo)
                    temp = search_and_add(source_key='longitude', container_key='longitude', container=temp, source=geo)

        server_data_results.append(temp.copy())  # python is linkedin crap that's why .copy()
        temp.clear()

    return server_data_results


def extract_search_data(server_data: dict) -> None | list[dict]:
    events = server_data.get('search_data').get('events')
    num_events = events.get('pagination').get('object_count')

    if int(num_events) == 0:
        print('no events found')
        return None

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



class SourceOneJsonParser:
    """Json Extractor"""

    """
    To all query types Source one generates different types of JSON server_data objects.
    However, both of them keep the information in particular keys.
    
    For Json structure A there's "jsonld" key
    For Json structure B there's "search_data" key
    
    The structure of overall JSON object may distinctly vary, however, we don't care about that.
    We need to look either for jsonld or search_data.
    
    "jsonld": the tag is in the root of JSON object => if "jsonld" in server_data: server_data.get("jsonld")
    "search_data": is also in the root of JSON object => same technique to detect it
    """

    @staticmethod
    def parse_server_data(server_data: dict) -> list[dict] | None:
        # go after jsonld
        if "jsonld" in server_data:
            return extract_jsonld(server_data)
        elif "search_data" in server_data:
            return extract_search_data(server_data)

