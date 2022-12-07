import streamlit as st
import streamlit_book as stb
from PIL import Image

st.set_page_config(
    page_title="Bitwalls",
    page_icon="🅱️",
)

# Streamlit book properties
stb.set_chapter_config(path="ecourse_streamlit",
                       toc=False,
                       button='top',
                       button_previous='◀',
                       button_next='▶',
                       button_refresh='🔄 ')

# Add a logo (optional) in the sidebar
logo = Image.open(r'logo.png')
st.sidebar.image(logo, width=200)
# Add two expanders to provide additional information about this e-tutorial and the app


with st.sidebar.expander("About Bitwalls"):
    st.write("""
        This interactive eCourse is designed to help beginner data analysts and data scientists to learn Python's most 
        popular data analysis library, Pandas, for their day-to-day analytics and data science work. 
     """)

with st.sidebar.expander("About this app"):
    st.write("""
        This interactive eCourse App was built by Sharone Li using Streamlit and Streamlit_book. Streamlit_book is a 
        Streamlit companion library that was written in Python and created by Sebastian Flores Benner. \n  
        \nThe Streamlit_book library was released on 01/20/2022. If you want to learn more about Streamlit_book, 
        please read Sebastian's post 
        here:https://blog.streamlit.io/how-to-create-interactive-books-with-streamlit-and-streamlit-book-in-5-steps/
     """)

# Create a user feedback section to collect comments and ratings from users
with st.sidebar.form(key='columns_in_form',
                     clear_on_submit=True):
    rating = st.slider("Please rate the app", min_value=1, max_value=5, value=3,
                       help='Drag the slider to rate the app. This is a 1-5 rating scale where 5 is the highest rating')
    text = st.text_input(label='Please leave your feedback here')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Thanks for your feedback!')
        st.markdown('Your Rating:')
        # st.markdown(rating)
        if rating == 1:
            st.markdown("⭐")
        elif rating == 2:
            st.markdown("⭐⭐")
        elif rating == 3:
            st.markdown("⭐⭐⭐")
        elif rating == 4:
            st.markdown("⭐⭐⭐⭐")
        else:
            st.markdown("⭐⭐⭐⭐⭐")

        st.markdown('Your Feedback:')
        st.markdown(text)

