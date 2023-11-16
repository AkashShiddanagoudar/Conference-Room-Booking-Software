import streamlit as st
import dataset2 as db2
import dataset as db


# Sample data


if 'record' not in st.session_state:
    st.session_state.record = db.record_meeting
# Initialize session state
if 'bookings' not in st.session_state:
    st.session_state.bookings = db2.requested_room
if 'available_room' not in st.session_state:     
    st.session_state.available_room=db2.available_room    
# if "x" not in st.session_state:
#     st.session_state.x=-1
# Function to book a room
# def remove_room(room_number):
#     if st.button("refersh"):
#         if(room_number==-1):
#             pass
#         else:
#             #st.write(room_number)
       
#             st.session_state.available_room.pop(room_number)
#         st.toast("updated")
            
        
    
   
def book_room(room):
    
    with st.expander(f"{room['RoomNumber']}"):
        project_name = st.text_input(f"Enter Project Name:{room['RoomNumber']}")
        num_people = st.number_input(f"Enter Number of People:{room['RoomNumber']}", min_value=1, step=1)
        
        if st.button(f"Book{room['RoomNumber']}"):
          
            
            
            booking_details = {
                'RoomNumber': room['RoomNumber'],
                'Date': room['Date'],
                'Time': room['Time'],
                'Status':"Pending",
                'Features': room['Features'],
                'Duration':room['Duration'],
                'ProjectTitle': project_name,
                'NumPeople': num_people
                
            }
            st.session_state.bookings.append(booking_details)
            st.session_state.record.append(booking_details)
            st.session_state.available_room.remove(room)
            st.toast("Room booked successfully!")
            st.experimental_rerun()
            

# Streamlit app
st.title("Available Rooms")
#remove_room(st.session_state.x)

for room in st.session_state.available_room:
    with st.expander(f"Room {room['RoomNumber']} - {room['Date']} {room['Time']} ({room['Duration']})", expanded=False):
        st.write(f"Features: {room['Features']}")
        book_room(room)
        

# Display booked rooms

st.title("Booked Rooms")
if st.session_state.bookings:
    for booking in st.session_state.record:
        st.write(f"Room {booking['RoomNumber']} - {booking['Date']} {booking['Time']}")
        st.write(f"Project Name: {booking['ProjectTitle']}")
        st.write(f"Number of People: {booking['NumPeople']}")
        st.write("---")
            

