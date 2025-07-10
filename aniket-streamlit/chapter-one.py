import streamlit as st

st.title("Pune one of the top hotels in India")
st.subheader("Welcome to Pune City")
st.text("what is required for you?")
st.write("Pune is a city in Maharashtra, India, known for its rich history, educational institutions, and vibrant culture. It is often referred to as the 'Oxford of the East' due to its numerous universities and colleges.")
food = st.selectbox(
    "Select your food",
    ("Choose","Puran Poli", "Misal Pav", "Vada Pav", "Bhel Puri", "Dhokla", "Samosa", "Pani Puri")
)
st.write (f"You have selected: {food}")

st.success ("Thank you for visiting our cafe!")
st.success("Pleaae visit again")

