import streamlit as st


def SideBarLinks(show_home=True):

    st.sidebar.image("https://rashidianlab.dana-farber.org/uploads/1/2/5/9/125925369/dfci-logo-lens-stacked1.png", width=150)
    
    st.sidebar.page_link("home.py", label="Home", icon="🏠")
    st.sidebar.page_link('pages/about.py', label="About", icon="🧫")
    st.sidebar.page_link('pages/get_duties.py', label="Generate Duties", icon="🔬")
    st.sidebar.page_link('pages/lab_members.py', label="Lab Members", icon="🧑‍🔬")
    st.sidebar.page_link('pages/lab_duties.py', label="Lab Duties", icon="🧪")
    st.sidebar.page_link('pages/projects.py', label='Projects', icon='🔮')




