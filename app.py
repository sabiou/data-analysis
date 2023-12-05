import streamlit as st
import pandas as pd
import altair as alt
import locale


# Set the locale to French
locale.setlocale(locale.LC_NUMERIC, 'fr_FR.UTF-8')

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

# Calculate percentages for each cell
percentage_table = (pivot_table.div(pivot_table.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_table['Percentage'] = (pivot_table['Total'] / pivot_table['Total'].loc['Total'] * 100).round(2)

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table.join(percentage_table['Percentage']))

# Create an Altair scatter chart
scatter_chart = alt.Chart(df).mark_circle().encode(
    x='ANNEE:N',
    y='QUANTITE A COMMANDER( BOITES):Q',
    color='Profil:N',
    tooltip=['Profil:N', 'ANNEE:N', 'QUANTITE A COMMANDER( BOITES):Q']
).properties(
    width=600,
    height=400
)

# Display the Altair scatter chart using Streamlit
st.write("## Scatter Chart")
st.altair_chart(scatter_chart, use_container_width=True)
