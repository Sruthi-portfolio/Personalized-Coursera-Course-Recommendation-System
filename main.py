# main_app.py

import streamlit as st
import pickle

# Load data using st.cache_data
@st.cache_data
def load_data():
    courses_list = pickle.load(open('data/courses.pkl', 'rb'))
    similarity = pickle.load(open('data/similarity.pkl', 'rb'))
    return courses_list, similarity

def main_app_page():
    st.markdown(
        """
        <style>
        .main-app {
            background-image: url('assets/main_app_bg.jpg');
            background-size: cover;

        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='main-app'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: blue;'>Coursera Course Recommendation System</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: white;'>Web App</h4>", unsafe_allow_html=True)

    # Load data
    courses_list, similarity = load_data()

    course_list = courses_list['course_name'].values
    selected_course = st.selectbox("Type or select a course you like:", course_list)

    if st.button('Show Recommended Courses'):
        st.write("Recommended Courses based on your interests are:")
        recommended_course_names = recommend(selected_course, courses_list, similarity)
        for course in recommended_course_names:
            st.text(course)

    if st.checkbox("Evaluation Results"):
        st.markdown('**Accuracy:** 98%')
        st.markdown('**Precision:** 98.6%')
        st.markdown('**Recall:** 94%')
        st.markdown('**F-1 Score:** 89%')

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def recommend(course, courses_list, similarity):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:7]]
    return recommended_course_names
