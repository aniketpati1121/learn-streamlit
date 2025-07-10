import streamlit as st

st.title("Chai Taste Poll") 
col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://t4.ftcdn.net/jpg/01/" \
    "66/87/43/360_F_166874362_kZTGg8x1JgRsSCJgO0GWhrkgSWa4ZqRA.jpg",width=90)
    vote1 = st.button("Vote for Masala Chai")
with col2: 
    st.header("Green Tea")
    st.image("https://www.aicr.org/wp-content/uploads/2020"
    "/06/peppermint-tea-on-teacup-1417945.jpg",width=90)
    vote2 = st.button("Vote for Green Tea")

if vote1:
    st.success("You voted for Masala Chai!")
elif vote2:
    st.success("You voted for Green Tea!")

name = st.sidebar.text_input("Enter your name:")
team = st.sidebar.selectbox("Select your Chai:", ["Masala", "Adarak", "Green", "Lemon", "Black"]) 
st.write(f"Hello, {name}! You selected {team} Chai.")  

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water in a pot.
    2. Add tea leaves and let it steep.
    3. Add milk and sugar to taste.
    4. Strain and serve hot.
    """)

    st.markdown('# Welcome to the Chai Taste Poll App!')
    st.markdown('>Blockquote: This app allows you to vote for your favorite type of chai and see the results in real-time.')

