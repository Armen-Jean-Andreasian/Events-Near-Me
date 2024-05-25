from app import *

location = Location("France")
entrance_fee = None #PaidEntrance()
event_category = None # BusinessCategory()
event_name = None #"Pool Party"  # if given  => server_data.get('search_data').get('events')
fixed_date = None  # Tomorrow()

custom_date_start = YYYYMMDDDate(year=2024, month=6, date=7)
custom_date_end = YYYYMMDDDate(year=2025, month=1, date=5)
custom_date = CustomDate(start_date=custom_date_start, end_date=custom_date_end)

save_raw_html = True
save_clear_html = True

use_server_data = True
use_react_query_state = True

events_app = EventsApp()

events = events_app.find_events(
    location=location,
    entrance_fee=entrance_fee,
    event_category=event_category,
    custom_event_name=event_name,
    fixed_date=fixed_date,
    custom_date=custom_date,
    save_raw_html=save_raw_html,
    save_clear_html=save_clear_html,
    use_server_data=use_server_data,
    # use_react_query_state=use_react_query_state
)
print(events)
