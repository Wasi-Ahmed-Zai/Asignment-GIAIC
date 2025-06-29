import streamlit as st

st.set_page_config(page_title="Explore with Python", page_icon="🌐", layout="centered")
st.title("🌟 Explore the Power of Python Web Apps")

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ About", "📬 Contact"])

if page == "🏠 Home":
    st.header("🏠 Welcome Home")
    st.write("You're on a Python-powered web app built with the simplicity of Streamlit!")
    name = st.text_input("👋 What's your name?")
    if name:
        st.balloons()
        st.success(f"Nice to meet you, {name}! Thanks for stopping by! 🚀")

elif page == "ℹ️ About":
    st.header("📖 About This App")  
    st.write("This interactive web app was crafted in less than 15 minutes using just Python and the awesome Streamlit library. Simple, fast, and fun!")

elif page == "📬 Contact":
    st.header("📬 Get in Touch")     
    email = st.text_input("📧 Enter your email")
    message = st.text_input("💬 Write your message here")
    if st.button("Send Message"):
        st.success("🎉 Thank you! Your message has been received. We'll get back to you soon.")



