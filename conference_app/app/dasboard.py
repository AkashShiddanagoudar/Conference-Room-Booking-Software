import streamlit as st
import pandas as pd
import dataset as db

import streamlit_nested_layout
if "notice_list" not in st.session_state:
        st.session_state.notice_list =db.office_notices

if 'record' not in st.session_state:
    st.session_state.record = db.record_meeting
        

def display_office_notices(office_notices):
    st.title("Office Notices")
#use checkbox  instead of button
    for notice in office_notices:
        with st.expander(f"Notice ID: {notice['Notice_ID']} - {notice['Subject']}"):
            st.empty()  # Clear previous content
            st.write(f"Content: {notice['Content']}")
            st.write(f"Department: {notice['Department']}")
         
def display():
    st.title("Requested Meetings Dashboard")

    # Display requested meetings information using st.expander
    for row in st.session_state.record:
        if( row['Date']=='2023-05-15'):
            col1, col2= st.columns([1,.2])
            with col1.expander(f"Meeting {row['RoomNumber']} - {row['ProjectTitle']}"):
                st.write(f"Status: {row['Status']}")
                st.write(f"Date: {row['Date']}")
                st.write(f"Time: {row['Time']}")
            with col2 :
                if row['Status'] == 'Accepted':
                    st.success('Accepted')
                elif row['Status'] == "Pending" :
                    st.warning("Pending")
                elif row['Status'] == "Denied" :
                    st.error("Denied")




# Convert the list of dictionaries to a Pandas DataFrame

# Streamlit app
st.title("Office Dashboard")

# Display Notices
with st.expander("Notice"):
        display_office_notices( st.session_state.notice_list)
    # You can add more interactivity or input elements for adding notices.

st.header("today meetings")
display()

