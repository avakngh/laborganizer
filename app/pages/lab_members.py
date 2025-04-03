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

def swap_members():
    '''
    Swap member duties between weeks given input "Name, Name"'''
    name1 = st.session_state.swap_member1
    name2 = st.session_state.swamp_member2
    #swap values
    st.session_state.members[[name1, 'Num']] = st.session_state.members[[name2, 'Num']]


# Add Member Section
add_name = st.text_input('Add New Lab Member (name and first initial)', key="add_name")
st.button('Add Member', on_click=add_member)

# Remove Member Section
remove_name = st.selectbox(label = 'Remove Lab Member (name and first initial)', options = st.session_state.members['Member'], key="remove_name")
st.button('Remove Member', on_click=remove_member)

# Skip Member Section
skip_member = st.selectbox(label = 'Skip a week for lab duties if lab member is unavailable:', options = st.session_state.members['Member'], key="skip_week")
st.button('Skip Week', on_click=skip_week)

# Swap lab member duties between weeks (IN PROGRESS)
swap_member1 = st.selectbox(label = 'Choose members to swap duties/weeks with', key="swap_member")
swap_member2 = st.selectbox('Choose members to swap duties/weeks with', key="swap_member")
st.button('Swap Members', on_click=swap_members)
