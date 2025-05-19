# password protection page
import streamlit as st
from modules.nav import unauthSideBar
import json
from pathlib import Path
import streamlit as st



st.set_page_config(layout='wide')

unauthSideBar()

ADMIN_FILE = Path("admin.json")

# Load admin credentials from JSON
if ADMIN_FILE.exists():
    with open(ADMIN_FILE, "r") as f:
        admin = json.load(f)
else:
    admin = {}

@st.dialog('Login as admin')
def login(page):
    st.write('Enter your admin username and password')
    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")

    if st.button('Submit'):
        if username_input in admin and str(admin[username_input]) == password_input:
            st.session_state.login = {'username': username_input}
            st.success("Login successful!")
            st.switch_page(page)
        else:
            st.warning('Incorrect username or password')


# Fancy background and welcome card
st.markdown("""
    <style>
    .parent-container {
        height: 50vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background: url('https://t4.ftcdn.net/jpg/02/33/72/65/360_F_233726552_Z4V3Mui929kKjgNqxieytcgoQbQ1ZCVz.jpg') center/cover no-repeat;
    }
    .centered-card {
        width: 60%;
        text-align: center;
        background: rgba(255, 255, 255, 0.7);
        padding: 30px;
        border-radius: 12px;
    }
    </style>
    <div class="parent-container">
        <div class="centered-card">
            <h1>Lab Duties Scheduler</h1>
            <p>Assign weekly tasks, view and edit lab members and duties, and adjust the weekly schedule as needed!</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation buttons
st.write('')
st.write('')


view_duties = st.button("Weekly Lab Duties",
             type='secondary',
             use_container_width=True)
if view_duties:
    st.switch_page('pages/get_duties.py')

members = st.button("View/Edit Lab Members",
             type='secondary',
             use_container_width=True)
if members:
    login('pages/lab_members.py')

edit_duties = st.button("View/Edit Lab Duties",
             type='secondary',
             use_container_width=True)
if edit_duties:
    login('pages/lab_duties.py')

projects = st.button('View Projects and Calendar',
                     type = 'secondary',
                     use_container_width=True)
if projects:
    st.switch_page('pages/projects.py')

edit_cal = st.button('Edit Calendar Events',
                     type = 'secondary',
                     use_container_width=True)

if edit_cal:
    login('pages/edit_calendar.py')

st.image('https://previews.dropbox.com/p/thumb/ACpeWPAJlTTspz2sDw5ksFqF-cfxgorzMH1cGMY2W6rVBSdGmr1skoDYr8bLn-I5wZyDeDlkjuEEWbsZIlxVAnhV3Ep8aPwjy-0kGUiQvF5UptWMJ8vx7KBzFch6LNTGdyRGKpkfKuzRLZythP7wNgUVsO1uzC-AyPQZHEuLDLk40bjVf5Awm1LktJC2ln9KZrZvNiAVNoKcmKFtEAbU78f6JYfsIAWgKIBuEEzmMm_lC6FHrMfjuWwGSdc48V5d5SW9kTE-Lryt0i1B4-364lbXVLAROb9YKiWWU0xYMKzycTDb13GenpIKgFtSAbvySEIvmaBiakpTrHbf3Ohj1tQIryhKgTtaK42DC2c8vKTM0jBK4vgCm7fPYOa4EmeCSRQo1WQkQxjkc16m4AxD7yu1UYGO4jHYOWFhmWqz8O2jKRnCcxOJcH4hl2Fmi_Nc3BwGs_zFzxWhIlGL2iQDwS52/p.jpeg',
         use_container_width=True)

with st.container():
    st.header('For admin:')
    user = st.text_input('Input Username')
    newpassword = st.text_input('Change Password', type="password")
    if st.button('Submit'):
        if user in admin:
            admin[user] = newpassword
            with open(ADMIN_FILE, "w") as f:
                json.dump(admin, f)
            st.success(f"Password for '{user}' updated successfully.")
        else:
            st.error(f"User '{user}' not found.")