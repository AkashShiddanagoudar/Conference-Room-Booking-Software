import streamlit as st
import json
import dataset as db
import dataset3 as db3
st.session_state.notice_list=db.office_notices
if "general_dataset" not in st.session_state:
    st.session_state.general_dataset=db3.general_dataset
if "notice_list" not in st.session_state:
        st.session_state.notice_list =st.session_state.notice_list

def display_notice_form():
    st.header("Notice Input Form")
    
    notice_id = st.text_input("Notice ID",value="")
    date = st.date_input("Date")
    subject = st.text_input("Subject",value="")
    content = st.text_area("Content",value="")
    department = st.text_input("Department",value="")

    notice_data = {
        "Notice_ID": notice_id,
        "Date": str(date),
        "Subject": subject,
        "Content": content,
        "Department": department
    }

    return notice_data

def main():
    st.title("Office Notice Dashboard")

    # Initialize session_state if not already present
   
    
    with st.expander('Post notice'):   

        notice_data = display_notice_form()

        if st.button("Add Notice"):
            st.session_state.notice_list.append(notice_data)
            st.toast("Notice added successfully!")
            
            
            

    if st.button("Show Notices"):
        st.header("List of Notices:")
        for notice in st.session_state.notice_list:
            st.write(notice)
            st.write("---")
   
    
    for meet in st.session_state.general_dataset:
        # if(meet['Date']=='2023-11-11'):
            with st.expander(f"{meet['ProjectTitle']} in {meet['RoomNumber']}"):
                c1,c2,c3=st.columns([.5, 1,.2])
                c1.write(f"{meet['ProjectTitle']}")
                c3.write(f"{meet['Time']}")
                

if __name__ == "__main__":
    main()
