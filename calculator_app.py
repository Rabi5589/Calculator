#calculator_app

import streamlit as st
import addition
import Subtraction
import multiplication
import division

def calculator():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:", step=0.1)
    num2 = st.number_input("Enter the second number:", step=0.1)
    operator = st.selectbox("Select the operator:", ["+", "-", "*", "/"])

    if st.button("Calculate"):
        if operator == "+":
            result = addition.add(num1, num2)
            st.write(f"Result: {result}")
        elif operator == "-":
            result = subtraction.subtract(num1, num2)
            st.write(f"Result: {result}")
        elif operator == "*":
            result = multiplication.multiply(num1, num2)
            st.write(f"Result: {result}")
        elif operator == "/":
            if num2 == 0:
                st.write("Error: Division by zero")
            else:
                result = division.divide(num1, num2)
                st.write(f"Result: {result}")
        else:
            st.write("Error: Invalid operator")

calculator()
