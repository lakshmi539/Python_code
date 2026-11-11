import streamlit as st
from donor_view import BloodDonorManager

donor_instance=BloodDonorManager()

tab1,tab2,tab3,tab4=st.tabs(["Add Donor","View Donors","Update Donors","Delete Donors"])
blood_groups=["A+","A-","B+","B-","AB+","AB-","O+","O-"]
with tab1:
    st.header("Add new Donor")
    name=st.text_input("Enter Donor Name")
    phone=st.text_input("Enter Donor Phone number")
    blood_group=st.selectbox("Select Blood Group",["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    city=st.text_input("Enter Donor city")
    last_donation=st.date_input("Enter last Donation date")
    if st.button("Submit"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Donor added successfully.")
with tab2:
    records = donor_instance.get()

    if records:
        st.table(records)
    else:
        st.warning("No members found...!")
with tab3:
    st.title("Update Donor details!")
    records=donor_instance.get()
    if records:
        donor_ids=[r[0] for r in records]
        id=st.selectbox("Select Donor ID",donor_ids,key="update_id")
        record=donor_instance.get_object(id=id)
        name=st.text_input("Enter your name:",value=record[1])
        phone=st.text_input("Enter your number:",value=record[3])
        blood_groups=st.selectbox("Select your blood group",blood_groups,
                        index=blood_groups.index(record[2]),
                        key="update_group")
        city=st.text_input("Enter your city:",value=record[4])
        last_donation=st.text_input("Enter your last donation:",value=record[5])
        if st.button("Update"):
            status,message=donor_instance.put(id=id,name=name,
                                phone=phone,
                                blood_group=blood_groups,
                                city=city,
                                last_donation=last_donation)
            if status:
                st.success(message)
            else:
                st.error(message)
    else:
        st.warning("No donor found")

