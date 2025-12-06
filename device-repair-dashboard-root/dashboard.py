import streamlit as st
import pandas as pd

def show_dashboard():
    st.title('Device Repair Dashboard')
    df = pd.read_csv('data/repairs.csv')
    st.dataframe(df)

    uploaded = st.file_uploader('Upload CSV/XLSX', type=['csv','xlsx'])
    if uploaded:
        if uploaded.name.endswith('.csv'):
            new_df = pd.read_csv(uploaded)
        else:
            new_df = pd.read_excel(uploaded)
        st.dataframe(new_df)
