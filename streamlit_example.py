import streamlit as st
  
def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("NA")
    else:
        return n*recur_factorial(n-1)

x = st.slider('Select a value')
st.write(x, 'Factorial is', recur_factorial(x))
