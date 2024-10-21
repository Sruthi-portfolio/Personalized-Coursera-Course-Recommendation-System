# login.py

import streamlit as st

def login_popup():
    st.markdown(
        """
        <style>
        .login-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 20px;
            border: 1px solid #ccc;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            z-index: 999;
            width: 300px;
            max-width: 90%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='login-popup'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: blue;'>Login</h2>", unsafe_allow_html=True)

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if authenticate(username, password):
            st.session_state.logged_in = True
        else:
            st.error('Invalid username or password. Please try again.')

    st.markdown("</div>", unsafe_allow_html=True)

def authenticate(username, password):
    # Replace with your actual authentication logic
    return username == "sv" and password == "611885"
