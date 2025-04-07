# projects
import streamlit as st
import pandas as pd

projects = pd.DataFrame(data = {'name': ['IL21', 'CAR NK', 'PV', 'Shreyas CD-19', 'BCMA CAR T', 'PET', 'Fibronectin'], 'num': list(range(7))})

if 'projects' not in st.session_state:
    st.session_state.projects = projects

st.title("Ongoing Projects:")
st.write(st.session_state.projects['name'])