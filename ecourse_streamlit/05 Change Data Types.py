import streamlit as st
import streamlit_book as st



# Add a single choice question
answer = st.single_choice("1. Which code below can be used to display the first 5 rows of a Pandas' data frame?",
                 options=["df.top(5)", "df.head(  )", "df.info(  )", "df.tail(  )"], answer_index=1)
