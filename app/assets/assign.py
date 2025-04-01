# assignment program
import pandas as pd
import streamlit as st

# lab members df
members = pd.DataFrame(data = {'Member': ['Shreya M.', 'Taha R.', 'Ali SF', 'Nili', 'Heydar M.', 'Leila M.',
                                          'Ukjae L.', 'Radia K.', 'Catie J.', 'Pegah T.', 'Martina W.', 'Yoon L.',
                                          'Victoria R.', 'Kamila M.', 'Ali V.', 'Valentina M.'], 
                               'Num': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]})

# lab duties df
duties = pd.DataFrame(data = {'duties': ['Lab JC', 'Break', 'Break', 'TC 1', 'Break', 'TC 2', 'Break', 'Break', 'Pipet Tips 1', 'Break', 'Pipet Tips 2', 'Break',
                                         'Mouse bodies + tools', 'Break', 'Break', 'Break']})


    
def assign():
    global members 

    # run twice for two weeks
    round = 1
    while round < 3:
        members['Num'] = (members['Num'] + 1) % len(members)
        st.write(f'Week {round}')
        assignments = members.merge(duties, left_on='Num', right_index=True, how='inner')
        assignments = assignments[['Member', 'duties']]
        st.write(assignments[assignments['duties'] != 'Break'])

        # Save updated values for week 1
        if round == 1:
            members_2 = members.copy()
        
        round += 1

    # Restore original values after running twice
    members = members_2
    return members, duties