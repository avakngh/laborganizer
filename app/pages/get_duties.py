# Generate Weekly Duties
import streamlit as st
from assets.assign import assign
from modules.nav import unauthSideBar
import datetime

# view_assignments.py
import streamlit as st
import pandas as pd
import os

unauthSideBar()

ASSIGNMENTS_FILE = "latest_assignments.csv"

st.title("Current Lab Assignments")
st.write(f'Today is {datetime.date.today()}')
st.write(f'If you need to make any changes due to a lab member`s availability one week, please see page "Lab Members."') 

if os.path.exists(ASSIGNMENTS_FILE):
    assignments = pd.read_csv(ASSIGNMENTS_FILE)
    for week in assignments['Week'].unique():
        st.subheader(week)
        st.dataframe(assignments[(assignments['Week'] == week) & (assignments['duties'] != 'Break')][['Member', 'duties']])

else:
    st.warning("No assignments found. Please run the update on a Monday.")

