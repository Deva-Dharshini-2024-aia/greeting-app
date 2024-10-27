import streamlit as st

st.title("Simple Greeting App")
name = st.text_input("Enter your name:")
message = st.text_input("Enter a short message:")
if name and message:
    st.write(f"Hello, **{name}**! 👋")
    st.write(f"Here's your message: *{message}*")
else:
    st.write("Please enter both your name and a message.")
