import streamlit as st
import dataset3 as db3
if "general_dataset" not in st.session_state:
    st.session_state.general_dataset=db3.general_dataset
def main():
    st.title("Available meets Dashboard")

    # Display available meets information using st.expander
    for meet in st.session_state.general_dataset:
        with st.expander(f"meet {meet['ProjectTitle']} - {meet['Date']} {meet['Time']}"):
            
            st.write(f"roomnuber: {meet['RoomNumber']}")
main()            
