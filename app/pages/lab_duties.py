# view/edit lab duties
import streamlit as st
from assets.assign import members, duties 
from modules.nav import SideBarLinks
import pandas as pd

SideBarLinks()

# Initialize session state for duties if not already set
if 'duties' not in st.session_state:
    st.session_state.duties = duties

if 'members' not in st.session_state:
    st.session_state.members = members

st.title("Current Lab Duties:")
st.write(st.session_state.duties[st.session_state.duties['duties'] != 'Break'])

st.write("If more than one person is needed for a particular lab duty, you can write 'Job 1', 'Job 2', etc so that if you need to reduce the number of positions later it doesn't delete all instances of the duty in the Dataframe")
add_duty = st.text_input('Add New Lab Duty')
submit_button1 = st.button('Add Duty')

# Text input for removing a duty
remove_duty = st.selectbox('Remove Lab Duty', options=st.session_state.duties['duties'])
submit_button2 = st.button('Remove Duty')

# Handle adding a duty
if submit_button1 and add_duty:
    st.session_state.duties.loc[len(st.session_state.duties)] = [add_duty]

    # Add a break in between to balance numbers
    if len(st.session_state.duties) < len(st.session_state.members):
        st.session_state.duties.loc[len(st.session_state.duties)] = ['Break']
    elif len(st.session_state.duties) > len(st.session_state.members):
        # Fix: Ensure correct structure when adding a new row to `members`
        new_row = pd.DataFrame({'Member': ['Space'], 'Num': [len(st.session_state.members)]})
        st.session_state.members = pd.concat([st.session_state.members, new_row], ignore_index=True)

# Handle removing a duty
if submit_button2 and remove_duty:
    index_to_remove = st.session_state.duties[st.session_state.duties['duties'] == remove_duty].index
    if not index_to_remove.empty:
        st.session_state.duties.drop(index_to_remove, inplace=True)
        st.session_state.duties.reset_index(drop=True, inplace=True)  # Reset index properly


