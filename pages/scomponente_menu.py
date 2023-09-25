import streamlit as st
from streamlit_option_menu import option_menu
import altair as alt
import pandas as pd
import streamlit as st


# 2. horizontal menu
def home():
   
   df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
   st.write(df)

def upload():
    df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
    st.write(df)

def tasks():
    st.write('Below is a DataFrame:')

def settings(): 
    st.write('Below is a DataFrame:')


selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Home":
    home()
elif selected2 == "Upload":
    upload()
elif selected2 == "Tasks":
    tasks()
elif selected2 == "Settings":
    settings()