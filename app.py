import streamlit as st
st.title('My Streamlit App - 21F1005467 - Assignment 8')
st.text('We will be doing addition of two numbers')
st.text('Type first number in the box below')
n1= st.number_input('Number',step=1,key="1")
st.text('Type second number in the box below')
n2 = st.number_input('Number',step=1,key="2")
st.write(f'{n1} + {n2} = {n1+n2}')
st.text("Thank you :)")
