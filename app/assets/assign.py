import pandas as pd
import streamlit as st
import datetime
from datetime import timedelta
import os

MEMBERS_FILE = "members_data.csv"
ASSIGNMENTS_FILE = "latest_assignments.csv"

# Load members
if os.path.exists(MEMBERS_FILE):
    members = pd.read_csv(MEMBERS_FILE)
else:
    members = pd.DataFrame({
        'Member': ['Shreya M.', 'Taha R.', 'Ali SF', 'Nili', 'Heydar M.', 'Leila M.',
                   'Ukjae L.', 'Radia K.', 'Catie J.', 'Pegah T.', 'Martina W.', 'Yoon L.',
                   'Victoria R.', 'Kamila M.', 'Ali V.', 'Valentina M.'],
        'Num': list(range(16))
    })

# Duties
duties = pd.DataFrame({'duties': ['Lab JC', 'Break', 'Break', 'TC 1', 'Break', 'TC 2', 'Break', 'Break',
                                  'Pipet Tips 1', 'Break', 'Pipet Tips 2', 'Break',
                                  'Mouse bodies + tools', 'Break', 'Break', 'Break']})

def assign():
    global members
    assignments_all = []

    for round in range(1, 3):
        members['Num'] = (members['Num'] + 1) % len(members)
        week_date = datetime.date.today() + timedelta(days=(round - 1) * 7)
        assignments = members.merge(duties, left_on='Num', right_index=True)
        assignments = assignments[['Member', 'duties']]
        assignments['Week'] = f"Week {round} ({week_date})"
        assignments_all.append(assignments)

    # Save updated state
    members.to_csv(MEMBERS_FILE, index=False)

    # Save current week's assignments
    final = pd.concat(assignments_all)
    final.to_csv(ASSIGNMENTS_FILE, index=False)
    return final[final['duties']!='Break']

st.title("Weekly Assignment Updater")

if datetime.date.today().weekday() == 0:  # Monday
    st.success("Today is Monday. Assignments updated!")
    # df = assign()
    # st.dataframe(df)
else:
    st.info("Assignments update only on Mondays.")
