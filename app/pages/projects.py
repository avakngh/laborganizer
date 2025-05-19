
import streamlit as st
import pandas as pd
from modules.nav import unauthSideBar
from streamlit_calendar import calendar
import uuid
import json
from pathlib import Path

def app():

    EVENTS_FILE = Path("events.json")

    # Load saved events from file
    if EVENTS_FILE.exists():
        with open(EVENTS_FILE, "r") as f:
            saved_events = json.load(f)
    else:
        saved_events = []

    # Initialize session_state["events"] with saved events
    if "events" not in st.session_state:
        st.session_state["events"] = saved_events


    # Initialize project list
    projects = pd.DataFrame(data={'name': ['IL21', 'CAR NK', 'PV', 'Shreyas CD-19', 'BCMA CAR T', 'PET', 'Fibronectin'], 'num': list(range(7))})
    if 'projects' not in st.session_state:
        st.session_state.projects = projects

    st.title("Ongoing Projects:")
    st.write(st.session_state.projects['name'])

    # Initialize session state
    if "event_added" not in st.session_state:
        st.session_state["event_added"] = False


    # Calendar options
    calendar_options = {
        "editable": True,
        "navLinks": True,
        "selectable": True,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridDay,dayGridWeek,dayGridMonth",
        },
        "initialDate": "2025-05-01",
        "initialView": "dayGridMonth"
        # "eventClick": """
        #     function(info) {
        #         const event = info.event;
        #         alert("Event: " + event.title + 
        #               "\\nStart: " + event.start.toDateString() + 
        #               "\\nEnd: " + event.end.toDateString() + 
        #               "\\nLocation: " + (event.extendedProps.location || "Not specified"));
        #     }
        # """
    }



    # Unique key to force calendar re-render
    if "Calendar" not in st.session_state:
        st.session_state["Calendar"] = str(uuid.uuid4())

    # Render calendar
    state = calendar(
        events=st.session_state["events"],
        options=calendar_options,
        custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
        """,
        key=st.session_state["Calendar"],
    )

    # Form to add a new event
    st.write('---')
    st.subheader('Enter a New Event')
    e_title = st.text_input('Add a title', key="e_title")
    e_cat = st.selectbox('Select an Event Category:', options=['Lab Meeting', 'Lab Member Unavailability', 'Seminar'], key="e_cat")
    e_start = st.date_input('Enter start date', key="e_start")
    e_end = st.date_input('Enter end date', key="e_end")
    e_location = st.selectbox('Meeting location', options=['Yawkey 308', 'Smith 7', 'TBD'], key='e_location')

    # Color mapping
    color_map = {
        'Lab Meeting': "#98e4ff",
        'Lab Member Unavailability': '#ff98ca',
        'Seminar': '#bffe80',
        'Yawkey 308': '##0f37ff',
        'Smith 7': '##00e72a',
        'TBD': '##e70000'
    }

    # Add new event
    if st.button("Schedule Event"):
        new_event = {
            "title": e_title,
            "start": str(e_start),
            "end": str(e_end),
            "allDay": True,
            "backgroundColor": color_map.get(e_cat, "#cccccc"),
            "borderColor": color_map.get(e_location, "#cccccc"),
            "extendedProps": {"location": e_location}
        }

        st.session_state['events'].append(new_event)

        with open(EVENTS_FILE, "w") as f:
            json.dump(st.session_state["events"], f)

        st.session_state["Calendar"] = str(uuid.uuid4())  # force rerender
        st.rerun()

    # Sync from calendar widget if user drags or edits events
    if state.get("eventsSet") is not None:
        if isinstance(state["eventsSet"], list):
            st.session_state["events"].extend(state["eventsSet"])
        elif isinstance(state["eventsSet"], dict):
            st.session_state["events"].append(state["eventsSet"])
