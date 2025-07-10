import streamlit as st

st.title("Chai Maker App") 
if st.button("Make Chai"):
    st.success("Your chai is being brewed!")

add_masala = st.checkbox("Do you want to add sugar?")  # <-- fixed typo

if add_masala:
    st.write("Masala added to your chai!") 

tea_type = st.radio("Pick your chai base:",["Milk","Water","Almond Milk","Coconut Milk"])
st.write(f"Selected chai base: {tea_type}") 
falavour = st.selectbox("Choose your chai flavour:", ["Cardamom", "Ginger", "Mint", "Lemon"])
st.write(f"Selected chai flavour: {falavour}")

sugar  = st.slider("How much sugar do you want?", 0 ,5 ,1)
st.write(f"You have added {sugar} teaspoons of sugar to your chai.") 
st.number_input("How many cups of chai do you want?", min_value=1, max_value=10, value=1) 

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Your chai is being prepared.")


dob = st.date_input("Enter your date of birth:")    
st.write(f"Your date of birth is: {dob}")

