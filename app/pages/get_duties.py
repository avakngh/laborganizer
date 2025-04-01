# Generate Weekly Duties
import streamlit as st
from assets.assign import assign, members, duties
from modules.nav import SideBarLinks

SideBarLinks()


st.title('Here are the lab assignments for the next two weeks!')
st.write(f'If you need to make any changes due to a lab member`s availability one week, please see page "Lab Members."') 
st.button("Get Weekly Assignment", on_click=assign) 

