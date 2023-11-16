
import streamlit as st
# st.session_state['abcd'] = fgjkhgkjhkujp
#'bookings'
requested_room =[
    {'RoomNumber': 501, 'Date': '2023-04-02', 'Time': '09:30', 'Status': 'Pending', 'Features': ['Whiteboard', 'Coffee Machine'], 'Duration': '1.5 hours', 'ProjectTitle': 'Team Workshop', 'NumPeople': 10},
    {'RoomNumber': 302, 'Date': '2023-04-05', 'Time': '14:45', 'Status': 'Pending', 'Features': ['Projector', 'Snacks'], 'Duration': '2 hours', 'ProjectTitle': 'Project Planning', 'NumPeople': 8},
    {'RoomNumber': 120, 'Date': '2023-04-08', 'Time': '11:00', 'Status': 'Pending', 'Features': ['Video Conferencing', 'Flip Chart'], 'Duration': '1 hour', 'ProjectTitle': 'Team Huddle', 'NumPeople': 6},
    {'RoomNumber': 410, 'Date': '2023-04-12', 'Time': '16:30', 'Status': 'Pending', 'Features': ['Laptop', 'Projector'], 'Duration': '1.5 hours', 'ProjectTitle': 'Training Session', 'NumPeople': 12},
    {'RoomNumber': 201, 'Date': '2023-04-15', 'Time': '10:15', 'Status': 'Accepted', 'Features': ['Whiteboard', 'Coffee Machine'], 'Duration': '1 hour', 'ProjectTitle': 'Discussion Meeting', 'NumPeople': 8},
    {'RoomNumber': 320, 'Date': '2023-04-18', 'Time': '13:00', 'Status': 'Denied', 'Features': ['Video Conferencing', 'Snacks'], 'Duration': '2 hours', 'ProjectTitle': 'Collaboration Session', 'NumPeople': 10},
]




#################################################
#'available_room'
available_room =[
    {'RoomNumber': 601, 'Date': '2023-04-22', 'Time': '08:45', 'Status': '', 'Features': ['Whiteboard', 'Coffee Machine'], 'Duration': '1.5 hours', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 412, 'Date': '2023-04-25', 'Time': '15:15', 'Status': '', 'Features': ['Projector', 'Snacks'], 'Duration': '2 hours', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 220, 'Date': '2023-04-28', 'Time': '10:30', 'Status': '', 'Features': ['Video Conferencing', 'Flip Chart'], 'Duration': '1 hour', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 510, 'Date': '2023-05-02', 'Time': '17:00', 'Status': '', 'Features': ['Laptop', 'Projector'], 'Duration': '1.5 hours', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 301, 'Date': '2023-05-05', 'Time': '09:45', 'Status': '', 'Features': ['Whiteboard', 'Coffee Machine'], 'Duration': '1 hour', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 420, 'Date': '2023-05-08', 'Time': '14:30', 'Status': '', 'Features': ['Video Conferencing', 'Snacks'], 'Duration': '2 hours', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 511, 'Date': '2023-05-12', 'Time': '12:15', 'Status': '', 'Features': ['Projector', 'Flip Chart'], 'Duration': '1.5 hours', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 230, 'Date': '2023-05-15', 'Time': '11:30', 'Status': '', 'Features': ['Laptop', 'Snacks'], 'Duration': '1 hour', 'ProjectTitle': '', 'NumPeople': 0},
    {'RoomNumber': 330, 'Date': '2023-05-18', 'Time': '13:45', 'Status': '', 'Features': ['Whiteboard', 'Coffee Machine'], 'Duration': '2 hours', 'ProjectTitle': '', 'NumPeople': 0},
]
