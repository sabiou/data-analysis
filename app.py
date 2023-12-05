import streamlit as st
import pandas as pd
import altair as alt


file_path = "database.xlsx"
df = pd.read_excel(file_path)


st.write("## Displaying DataFrame")
st.write(df)


# Create a pivot table
pivot_table = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['Profil'],
    columns=['ANNEE'],
    aggfunc={'QUANTITE A COMMANDER( BOITES)': 'sum'},
    margins=True,
    margins_name='Total'
)

# Calculate percentages only for the 'Total' column
percentage_table = (pivot_table.div(pivot_table.iloc[:, -1], axis=0) * 100).round(2)

# Display the pivot table using Streamlit
st.write("## Pivot Table")
st.write(pivot_table)
