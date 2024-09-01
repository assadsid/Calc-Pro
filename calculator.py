import streamlit as st

# Title of the app
st.title("Python Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Select operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on the selected operation
# if st.button("Calculate"):
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
    # if result is not None:
    #     st.success(f"The result is: {result}")

# Footer
st.write("Result:", result)
# st.write("Simple calculator app using Streamlit")
