import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')


st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #fbcaff, #e5c3ff, #c3c4ff);
        font-family: 'Helvetica', sans-serif;
        margin: 0;
        padding: 0;
    }

    .parent-container {
        position: relative;
        width: 100%;
        height: 50vh; /* Make sure it fills the full screen */
        display: flex;
        justify-content: center;
        align-items: center;
        
        /* Force background image to fill */
        background: url('https://t4.ftcdn.net/jpg/02/33/72/65/360_F_233726552_Z4V3Mui929kKjgNqxieytcgoQbQ1ZCVz.jpg') no-repeat center center;
        background-size: cover;
        
        z-index: 1; /* Keep it behind other elements */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    .centered-card {
        width: 60%;
        text-align: center;
        position: relative; /* Ensure it stays over the background */
        background: rgba(255, 255, 255, 0.7); /* Slight transparency to see background */
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        z-index: 2; /* Ensures it's above the background */
    }

    h1 {
        color: #333;
        font-size: 28px;
    }

    p {
        font-size: 16px;
        color: #555;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="parent-container">
        <div class="centered-card">
            <h1>Lab Duties Scheduler</h1>
            <p>Assign weekly tasks, view and edit lab members and duties, and adjust the weekly schedule as needed!</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write('')
st.write('')


if st.button("Weekly Lab Duties",
             type='secondary',
             use_container_width=True):
    st.switch_page('pages/get_duties.py')

if st.button("View/Edit Lab Members",
             type='secondary',
             use_container_width=True):
    st.switch_page('pages/lab_members.py')

if st.button("View/Edit Lab Duties",
             type='secondary',
             use_container_width=True):
    st.switch_page('pages/lab_duties.py')

SideBarLinks(show_home=True)