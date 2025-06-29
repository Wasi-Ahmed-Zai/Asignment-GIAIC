import streamlit as st
import os
import hashlib
import sqlite3
from cryptography.fernet import Fernet

KEY_FILE = "simple_secure.key"

# Load or generate key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
    else:
        with open(KEY_FILE, "rb") as file:
            key = file.read()
    return key

cipher = Fernet(load_key())

# Initialize database
def initial_database():
    connect = sqlite3.connect("simple_data.db")
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vault (
            label TEXT PRIMARY KEY,
            encrypted_text TEXT,
            passkey TEXT
        )
    """)
    connect.commit()
    connect.close()

initial_database()

# Hashing function
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encryption function
def encrypt_text(text):
    return cipher.encrypt(text.encode()).decode()

# Decryption function
def decrypt_text(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# Streamlit UI
st.title("🔐 Secure Data Encryption App")

menu = ["Store Secret", "Retrieve Secret"]
choice = st.sidebar.selectbox("Choose Option:", menu)

# Store secret
if choice == "Store Secret":
    st.header("Store a New Secret")

    label = st.text_input("Label (Unique ID):")
    secret = st.text_area("Your Secret:")
    passkey = st.text_input("Passkey (to protect it):", type="password")

    if st.button("Encrypt and Save"):
        if label and secret and passkey:
            connect = sqlite3.connect("simple_data.db")
            cursor = connect.cursor()

            encrypted = encrypt_text(secret)
            hashed_key = hash_passkey(passkey)

            try:
                cursor.execute("INSERT INTO vault (label, encrypted_text, passkey) VALUES (?, ?, ?)",
                               (label, encrypted, hashed_key))
                connect.commit()
                st.success("✅ Secret saved successfully!")
            except sqlite3.IntegrityError:
                st.error("❌ Label already exists. Please choose another.")
            connect.close()
        else:
            st.warning("⚠️ Please fill all the fields!")

# Retrieve secret
elif choice == "Retrieve Secret":
    st.header("Retrieve Your Secret")

    label = st.text_input("Enter Label:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        connect = sqlite3.connect("simple_data.db")
        cursor = connect.cursor()
        cursor.execute("SELECT encrypted_text, passkey FROM vault WHERE label=?", (label,))
        result = cursor.fetchone()
        connect.close()

        if result:
            encrypted_text, stored_hash = result
            if hash_passkey(passkey) == stored_hash:
                decrypted = decrypt_text(encrypted_text)
                st.success("🔓 Here is your secret:")
                st.code(decrypted)
            else:
                st.error("❌ Incorrect passkey.")
        else:
            st.warning("⚠️ No record found for the given label.")

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p style="font-size: 16px; text-transform: uppercase;">
            Developed  with ❤️  by 
            <a href="https://github.com/wasi881" target="_blank" style="text-decoration: none; color: #4CAF50; font-weight: bold;">
                WASI AHMED
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
