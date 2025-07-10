import streamlit as st


st.title("Chai Maker App") 
if st.button("Make Chai"):
    st.success("Your chai is being brewed!")

add_masala = st.chechbox("Do you want to add sugar?")  

if add_masala:
    st.write("Masala added to your chai!")


