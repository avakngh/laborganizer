# about
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()


st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #FFEECC, #CCFFFF, #EECCFF);
        font-family: 'Helvetica', sans-serif;
    }

    .parent-container {
        position: relative;
        width: 100%;
        z-index: 1; /* Ensure parent container has a higher stacking context */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: -50px;
    }

    .centered-card {
        margin: 35px;
        margin-top: 90px;
        position: absolute;
        background: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        z-index: 2;
    } 

    .centered-card h1 {
        font-size: 2.8em;
        font-family: monospace;
        margin-bottom: 20px;
    }

    .centered-card p {
        font-size: 0.9rem;
        margin-bottom: 30px;
        color: #555;
    }

    .centered-card ul {
        margin-bottom: 30px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="parent-container">
    <div class="centered-card">
        <h1>Your Lab Duties Scheduler: About and How to Use</h1>

<h5>Here, you can view and edit lab members and duties, organize weekly tasks, and adjust the schedule based on lab members' needs. Let's break it down.</h5>
<hr/>

<h3>Generate Duties:</h3>
<p>On this page, you will get weekly assignments for each lab duty. The algorithm is based on a number assignment system where each lab member has a number that is associated with a particular lab duty. Each week, these numbers are cycled through so a different person is assigned a new duty when their number is called. Week 1 of the generated list is "this week" and week two is "next week." At the beginnning of "next week," when you need to reprint assignments for the upcoming week, Week 1's print-out is updated as the current week (week 2 from the previous week) and Week 2 is now for next week. </p>

<h3>Lab Members:</h3>
<p>This page allows you to view and edit current lab members. Each lab member is listed with a first name and last initial (usually followed by a period), so try to keep this trend when adding new names for ease of removal later. If you don't type a name exactly as it's shown, ex. Shreya M instead of Shreya M., it'll produce an error. I can try to fix this too if it's too annoying but I was feeling kind of lazy.</p>

<h3>Lab Duties:</h3>
<p>This page allows you to view and edit current duties in the lab. You can add or remove jobs as needed. If a job requires more than one person, I recommend adding a 1, 2, etc. after the name so that if you need to remove this duty or lessen the amount of members needed to complete it, you don't remove all of the instances of the job in the dataframe. If that's annoying I can also fix it probably.</p>

    """,
    unsafe_allow_html=True,)