import streamlit as st
import dataset2 as db2
import dataset as db
import dataset3 as db3
import pandas as pd

# Your list of pending meetings
if 'bookings' not in st.session_state:
    st.session_state.bookings = db2.requested_room

if 'record' not in st.session_state:
    st.session_state.record = db.record_meeting
if 'available_room' not in st.session_state:     
    st.session_state.available_room=db2.available_room     
# Function to update the status of a meeting
def update_status(meeting, new_status):
    meeting['Status'] = new_status
if "general_dataset" not in st.session_state:
    st.session_state.general_dataset=db3.general_dataset
# Streamlit app
def pending_meetings():
    st.title('Pending Meetings')

    for meeting in st.session_state.bookings :
        c1,c2 =st.columns([1,.2])
        if(meeting['Status']=="Pending"):
            with c1.expander(f"{meeting['ProjectTitle']} - Room {meeting['RoomNumber']}"):
                st.write(f"Date: {meeting['Date']} | Time: {meeting['Time']}")
                st.write(f"Status: {meeting['Status']}")
                
                btn_approve = st.button(f"Approve meeting{meeting['ProjectTitle']}")
                btn_decline = st.button(f"Decline meeting {meeting['ProjectTitle']}")

                if btn_approve:
                    update_status(meeting, 'Accepted')
                    st.session_state.record[st.session_state.record.index(meeting)]['Status']= 'Accepted'
                    st.session_state.general_dataset.append(meeting)
                    st.success("Meeting Approved!")
                    st.write(f"Updated Status: {meeting['Status']}")
                    st.experimental_rerun()
                    

                if btn_decline:
                    update_status(meeting, 'Denied')
                    st.session_state.record[st.session_state.record.index(meeting)]['Status']= 'Denied'
                    st.session_state.available_room.append(meeting)
                    st.warning("Meeting Declined!")
                    st.write(f"Updated Status: {meeting['Status']}")
                    st.experimental_rerun()
            with c2 :
                st.warning("Pending")
                
def accepted_meetigs():
    for meeting in st.session_state.bookings :
        
        if(meeting['Status']=='Accepted'):
            c1,c2 =st.columns([1,.2])
            with c1.expander(f"{meeting['ProjectTitle']} - Room {meeting['RoomNumber']}"):
                st.write(f"Date: {meeting['Date']} | Time: {meeting['Time']}")
                st.write(f"Status: {meeting['Status']}")
            with c2 :
               st.success('Accepted')
                               
def denied_meetigs():
    for meeting in st.session_state.bookings :
       
        if(meeting['Status']=='Denied'):
            c1,c2 =st.columns([1,.2])
            with c1.expander(f"{meeting['ProjectTitle']} - Room {meeting['RoomNumber']}"):
                st.write(f"Date: {meeting['Date']} | Time: {meeting['Time']}")
                st.write(f"Status: {meeting['Status']}")
            with c2 :
               st.error('Denied')     
    
# st.table(pd.DataFrame(st.session_state.bookings ))            
                
def main():
    selected_status = st.selectbox("meetings", ["Pending", "Accepted",'Denied'])
    if(selected_status=="Pending"):
       pending_meetings()
    elif(selected_status=="Accepted"):
       accepted_meetigs()
    elif(selected_status=='Denied'):
       denied_meetigs()                    

if __name__ == '__main__':
    main()
