import streamlit as st
from app import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.tools.models import ResponseModel

# taking input
NOT_CHOSEN_CHAR = "---"

st.title('Events Near Me!')

st_location = st.text_input(label="Enter your location:",
                            placeholder="Example: Country, City, Region, Address, any other location",
                            help="Enter a location. Example: Madrid",
                            key="location").strip()

st_event_name = st.text_input(label="Enter the name of event (optional): ",
                              placeholder="Example: Pool Party",
                              help="If you are looking for a specific event/s enter the name, or leave it blank",
                              key="event_name").strip()

st_entrance_fee = st.selectbox(label="Choose the entrance fee (optional): ",
                               options=(NOT_CHOSEN_CHAR, PaidEntrance(), FreeEntrance()),
                               help="You can leave empty if you want to see both paid and free events.",
                               key='entrance_fee')

st_event_category = st.selectbox(label="Choose the event category (optional):",
                                 help="You can leave empty if you want to see the events of all categories.",
                                 options=(NOT_CHOSEN_CHAR, BusinessCategory(),),
                                 key='event_category')

st_fixed_date = st.selectbox(
    label="Fixed Date (optional):",
    help="You can leave empty if you want to see all events.",
    options=(NOT_CHOSEN_CHAR, Today(), Tomorrow(), ThisWeekend())
)

st_checkbox_offline_only: bool = st.checkbox(label="Offline events only")

custom_date_start = None
custom_date_end = None
fixed_date = None

if st.button('Select Custom Date Period'):
    custom_date_start = st.date_input(label='Choose start date')
    custom_date_end = st.date_input(label='Choose end date')

process_button = st.button("Find events")

# finding events
if process_button:
    with st.spinner("Processing"):

        # analyzing
        if st_location:
            location: Location = Location(st_location)
        else:
            st.error("Location can't be empty!")
            exit()

        event_name: str | None = st_event_name if st_event_name else None
        entrance_fee: FreeEntrance | PaidEntrance | None = st_entrance_fee if st_entrance_fee != NOT_CHOSEN_CHAR else None
        event_category: BusinessCategory | None = st_event_category if st_event_category != NOT_CHOSEN_CHAR else None

        if custom_date_start and custom_date_end:
            fixed_date = None
            custom_date = CustomDate(start_date=custom_date_start, end_date=custom_date_end)
        else:
            custom_date = None
            fixed_date = st_fixed_date if st_fixed_date != NOT_CHOSEN_CHAR else None

            # processing
            events_app = EventsApp()
            events: "ResponseModel" = events_app.find_events(
                location=location,
                entrance_fee=entrance_fee,
                event_category=event_category,
                custom_event_name=event_name,
                fixed_date=fixed_date,
                custom_date=custom_date,
                # unnecessary for user => hardcoded
                save_raw_html=True,
                # save_clear_html=True,
                # use_server_data=True,
            )

            st.write(events.status_code, events.status)

            if events.status_code != 200:
                st.warning(events.message)
                st.warning(events.description)

            else:
                # displaying results

                st.success("Results:")
                results: list[dict] = events.model_dump().get("data")


                def display_event_details(event_container):
                    if "name" in event_container:
                        st.subheader(event_container.get("name"))

                    if "image" in event_container:
                        st.image(event_container.get("image"))

                    if "description" in event_container:
                        st.write(event_container.get("description"))

                    if "start_date" and "end_date" in event_container:
                        st.write(
                            "Dates: {start_date} - {end_date}".format(
                                start_date=event_container.get("start_date"),
                                end_date=event_container.get("end_date")
                            ))


                def display_event_location(event_container):
                    st.write(
                        "Address: {address_1}, {country}, {city}, {region}, {postal_code}".format(
                            address_1=event_container.get("address_1"),
                            country=event_container.get("country"),
                            city=event_container.get("city"),
                            region=event_container.get("region"),
                            postal_code=event_container.get("postal_code")
                        )
                    )
                    with st.expander(label="See on maps"):
                        # maps should be implemented, as st.maps is trash
                        st.write("Maps are under construction")


                for event_container in results:
                    st.divider()

                    if st_checkbox_offline_only:  # checkbox - location only. else : any
                        if ("country" and "city" and "region" and "postal_code" and "address_1" and "latitude" and "longitude") in event_container:
                            display_event_details(event_container)
                            display_event_location(event_container)
                        else:
                            continue  # skipping the event as it's online and "offline only" is checked

                    else:  # displaying event details only
                        display_event_details(event_container)
