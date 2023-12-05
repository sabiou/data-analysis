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


# Create a pivot table with 'DEMANDEUR' as the index
pivot_table_demandeur = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['DEMANDEUR'],
    columns=['ANNEE'],
    aggfunc={'QUANTITE A COMMANDER( BOITES)': 'sum'},
    margins=True,
    margins_name='Total'
)

# Calculate percentages for each cell
percentage_table_demandeur = (pivot_table_demandeur.div(pivot_table_demandeur.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_table_demandeur['Percentage'] = (pivot_table_demandeur['Total'] / pivot_table_demandeur['Total'].loc['Total'] * 100).round(2)

# Display the new pivot table with original values and percentage using Streamlit
st.write("## Pivot Table with DEMANDEUR as Index")
st.write(pivot_table_demandeur.join(percentage_table_demandeur['Percentage']))

