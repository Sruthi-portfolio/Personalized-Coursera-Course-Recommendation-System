import streamlit as st
from login import login_popup
from main import main_app_page

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Set page title and layout
st.set_page_config(page_title="Course Recommendation System", layout="wide")

# Display login popup if not logged in
if not st.session_state.logged_in:
    login_popup()
else:
    main_app_page()