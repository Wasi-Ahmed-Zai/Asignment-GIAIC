import streamlit as st
import re


st.title("Password Strength Meter")
def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        st.error("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.error("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        st.info("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.info("❌ Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")


password = st.text_input("Enter your password: ", type="password")

if st.button("Check Password"):
    check_password_strength(password)
