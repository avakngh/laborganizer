# projects
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from streamlit_calendar import calendar

SideBarLinks()

projects = pd.DataFrame(data = {'name': ['IL21', 'CAR NK', 'PV', 'Shreyas CD-19', 'BCMA CAR T', 'PET', 'Fibronectin'], 'num': list(range(7))})

if 'projects' not in st.session_state:
    st.session_state.projects = projects

st.title("Ongoing Projects:")
st.write(st.session_state.projects['name'])

# Default events
import streamlit as st
from streamlit_calendar import calendar

# --- Initialize session state variables ---
if "event_added" not in st.session_state:
    st.session_state["event_added"] = False

if "events" not in st.session_state:
    # Initialize with some default events
    st.session_state["events"] = [
        {
            "title": "Fibronectin",
            "backgroundColor": "#4389d9",
            "start": "2025-04-08",
            "end": "2025-04-08",
            "borderColor": "#4389d9",
        },
        {
            "title": "IL21",
            "backgroundColor": "#4389d9",
            "start": "2025-04-15",
            "end": "2025-04-15",
            "borderColor": "#4389d9",
        },
        {
            "title": "Shreyas CD19",
            "backgroundColor": "#4389d9",
            "start": "2025-04-22",
            "end": "2025-04-22",
            "borderColor": "#4389d9",
        },
    ]

# --- Calendar options ---
calendar_options = {
    "editable": True,
    "navLinks": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridDay,dayGridWeek,dayGridMonth",
    },
    "initialDate": "2025-04-01",
    "initialView": "dayGridMonth",
}

# --- Calendar display ---
state = calendar(
    events=st.session_state["events"],
    options=calendar_options,
    custom_css="""
    .fc-event-past { opacity: 0.8; }
    .fc-event-time { font-style: italic; }
    .fc-event-title { font-weight: 700; }
    .fc-toolbar-title { font-size: 2rem; }
    """,
    key="calendar"
)

# --- Event Adding Logic ---
def addEvent():
    title = st.session_state["e_title"]
    category = st.session_state["e_cat"]
    start = st.session_state["e_start"]
    end = st.session_state["e_end"]

    color_map = {
        "Lab Meeting": "#4389d9",
        "Lab Member Unavailability": "#e368b0",
        "Seminar": "#5bb595"
    }

    new_event = {
        "title": title,
        "start": str(start),
        "end": str(end),
        "allDay": True,
        "backgroundColor": color_map.get(category, "#cccccc"),
        "borderColor": color_map.get(category, "#cccccc"),
    }

    # Add the new event to the list
    st.session_state["events"].append(new_event)

    # Set flag so rerun happens only once
    st.session_state["event_added"] = True
    st.experimental_rerun()

# --- Input Fields ---
st.write('Enter a New Event')
e_title = st.text_input('Add a title', key="e_title")
e_cat = st.selectbox('Select an Event Category:', options=['Lab Meeting', 'Lab Member Unavailability', 'Seminar'], key="e_cat")
e_start = st.date_input('Enter start date', key="e_start")
e_end = st.date_input('Enter end date', key="e_end")

# --- Submit Button ---
e_submit = st.button('Schedule Event', on_click=addEvent)

# --- Reset flag after rerun ---
if st.session_state.get("event_added"):
    st.session_state["event_added"] = False

