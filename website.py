import streamlit as st
st.title("welcome to learn python tutorial")
st.header("learn python from scratch")
st.subheader("starting the course")
st.markdown("We are starting with the project which will print the first 10 multiples of the number input by the user!")
st.code("""num = int(input("enter your number  :"))
        for i in range(1, 11):
            print(f"{num}X{i}={num*i}")
        """)
name = st.text_input("Enter your name")
Fname = st.text_input("Enter your father name")
adr = st.text_area("Enter your full address")
age = st.selectbox("Enter your age :",(18,19,20,21,22,23,24,25))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father name : {Fname}
    Address : {adr}
    Age : {age}""")


