import streamlit as st


def SideBarLinks(show_home = True):

    st.sidebar.image("https://rashidianlab.dana-farber.org/uploads/1/2/5/9/125925369/dfci-logo-lens-stacked1.png", width=150)
    
    st.sidebar.page_link("home.py", label="Login", icon="🏠")
    st.sidebar.page_link('pgs/about.py', label="About", icon="🧫")
    st.sidebar.page_link('pgs/get_duties.py', label="View Lab Duties", icon="🔬")
    st.sidebar.page_link('pgs/lab_members.py', label="Lab Members", icon="🧑‍🔬")
    st.sidebar.page_link('pgs/lab_duties.py', label="Edit Lab Duties", icon="🧪")
    st.sidebar.page_link('pgs/projects.py', label='Projects', icon='🔮')
    st.sidebar.page_link('pgs/edit_calendar.py', label='Edit Events', icon='🔧')

def unauthSideBar(show_home = True):
    st.sidebar.image("https://rashidianlab.dana-farber.org/uploads/1/2/5/9/125925369/dfci-logo-lens-stacked1.png", width=150)
    
    st.sidebar.page_link("home.py", label="Login", icon="🏠")
    st.sidebar.page_link('pgs/about.py', label="About", icon="🧫")
    st.sidebar.page_link('pgs/get_duties.py', label="View Lab Duties", icon="🔬")
    st.sidebar.page_link('pgs/projects.py', label='Projects', icon='🔮')