import streamlit as st
from modules.nav import SideBarLinks
import uuid
import json
from pathlib import Path
from datetime import datetime

SideBarLinks()

# Color map
color_map = {
    'Lab Meeting': "#98e4ff",
    'Lab Member Unavailability': '#ff98ca',
    'Seminar': '#bffe80',
    'Yawkey 308': '#0f37ff',
    'Smith 7': '#00e72a',
    'TBD': '#e70000'
}

# Load events from file
EVENTS_FILE = Path("events.json")
if EVENTS_FILE.exists():
    with open(EVENTS_FILE, "r") as f:
        saved_events = json.load(f)
else:
    saved_events = []

# Ensure all events have 'end' and 'title'
for e in saved_events:
    if "end" not in e:
        e["end"] = e["start"]  # fallback
    if "title" not in e:
        e["title"] = "(Untitled)"


# Initialize Streamlit page
st.title("Edit Events")

# Make list of event labels for selection
event_titles = [f"{i + 1}. {e['title']} ({e['start']})" for i, e in enumerate(saved_events)]

# Select event
selected_index = st.selectbox("Pick event to edit", options=list(range(len(event_titles))), format_func=lambda i: event_titles[i])

# Get the selected event
event = saved_events[selected_index]

# Editable fields
new_title = st.text_input("Change Event Title", value=event["title"])
new_start = st.date_input("Change Start Date", value=datetime.strptime(event["start"], "%Y-%m-%d").date())
default_end = event.get("end", event["start"])  # fallback to start date if end is missing
new_end = st.date_input("Change End Date", value=datetime.strptime(default_end, "%Y-%m-%d").date())
location = st.selectbox("Change Location/Meeting", options=list(color_map.keys()))
new_color = color_map[location]

# Submit changes
if st.button("Save Changes"):
    event["title"] = new_title
    event["start"] = new_start.isoformat()
    event["end"] = new_end.isoformat()
    event["backgroundColor"] = new_color
    event["borderColor"] = new_color
    event["extendedProps"]["location"] = location

    # Save all events back to file
    with open(EVENTS_FILE, "w") as f:
        json.dump(saved_events, f, indent=4)

    st.success("Event updated successfully!")

