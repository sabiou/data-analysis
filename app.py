import streamlit as st
import pandas as pd
import altair as alt


file_path = "database.xls"
df = pd.read_excel(file_path)


st.write("## Displaying DataFrame")
st.write(df)
