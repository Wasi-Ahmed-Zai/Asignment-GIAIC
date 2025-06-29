import streamlit as st

st.title("🧮 BMI Calculator")

weight = st.number_input("Enter your weight in kg: ")
feet = st.number_input("Enter your height in feet:")
height_cm = feet * 30.48
height_m = height_cm / 100
final_height = height_m ** 2

if st.button("Calculate BMI"):
    if final_height == 0:
        st.error("❗ Height cannot be zero.")
    else:
        bmi = weight / final_height
        st.success(f"✅ Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("⚠️ You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("😊 You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight.")
        else:
            st.error("❗ You are obese.")



