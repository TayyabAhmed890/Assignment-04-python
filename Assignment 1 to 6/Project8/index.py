import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Streamlit UI setup
def main():
    # Title and Description
    st.title("BMI Calculator")
    st.write("Welcome to the BMI calculator! This app will help you calculate your Body Mass Index (BMI).")

    # Get user's weight and height input
    weight = st.number_input("Enter your weight in kg (e.g., 70)", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height in meters (e.g., 1.75)", min_value=0.1, step=0.01)

    # Calculate BMI when the user clicks the button
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            # Show the result
            st.write(f"Your BMI is: {bmi:.2f}")
            
            # Determine the BMI category
            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
        else:
            st.write("Please enter valid weight and height.")

# Run the main function
if __name__ == "__main__":
    main()
