# view/edit lab members
import streamlit as st 
from assets.assign import members, duties
from modules.nav import SideBarLinks

SideBarLinks()

if "members" not in st.session_state:
    st.session_state.members = members

st.title('Rashidian Lab Members')
st.write('Edit current and inactive lab members, or skip someones weekly duties if they are unavailable!')


st.text('Current Rashidian Lab Members:')
st.text("\n".join(st.session_state.members['Member']))

def add_member():
    if 'Space' in st.session_state.members['Member'].values:
        st.session_state.members.loc[
            st.session_state.members['Member'] == 'Space', 'Member'
        ] = st.session_state.add_name
    else:
        new_index = len(st.session_state.members)
        st.session_state.members.loc[new_index] = [st.session_state.add_name, new_index]

def remove_member():
    # Filter out the member to remove and reset index
    st.session_state.members = st.session_state.members[
        st.session_state.members['Member'] != st.session_state.remove_name
    ].reset_index(drop=True)

def skip_week():
    st.session_state.members['Num'] = (st.session_state.members['Num'] + 1) % len(st.session_state.members)

# Add Member Section
add_name = st.text_input('Add New Lab Member (name and first initial)', key="add_name")
st.button('Add Member', on_click=add_member)

# Remove Member Section
remove_name = st.text_input('Remove Lab Member (name and first initial)', key="remove_name")
st.text('Make sure to watch your spelling or it will raise an error!')
st.button('Remove Member', on_click=remove_member)

# Skip Member Section
skip_member = st.text_input('Choose who to skip for weekly lab duties if lab member is unavailable:', key="skip_member")
st.button('Skip Member', on_click=skip_week)
