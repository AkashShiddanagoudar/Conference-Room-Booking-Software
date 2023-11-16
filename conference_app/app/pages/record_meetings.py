import streamlit as st
import pandas as pd
import dataset as db



# Convert the list of dictionaries to a DataFrame
if 'record' not in st.session_state:
    st.session_state.record = db.record_meeting

def main():
    st.title("Requested Meetings Dashboard")

    # Display requested meetings information using st.expander
    for row in st.session_state.record:
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

if __name__ == "__main__":
    main()
