import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Select Page:', ('EDA', 'Prediction'))

if page == 'EDA':
    try:
        eda.run()
    except Exception as e:
        st.error(f"An error occured in EDA: {e}")
else:
    try:
        prediction.run()
    except Exception as e:
        st.error(f"An error occured in Prediction: {e}")
