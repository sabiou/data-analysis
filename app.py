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


# Filter the data for the value "Centrale pharmaceutique" in the "Profil" column
data_centrale = df[df['Profil'] == 'Centrale pharmaceutique']

# Remove spaces from column names in data_centrale
data_centrale.columns = data_centrale.columns.str.strip()

# Get unique DEMANDEUR values corresponding to Centrale pharmaceutique
demandeurs_centrale = data_centrale['DEMANDEUR'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to Centrale pharmaceutique in the DEMANDEUR column
df_centrale_records = df[df['DEMANDEUR'].isin(demandeurs_centrale)]

# Create a pivot table for the new DataFrame
pivot_table_all_records = df_centrale_records.pivot_table(
    index='DEMANDEUR', 
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records['Total'] = pivot_table_all_records.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records['Percentage'] = (pivot_table_all_records['Total'] / pivot_table_all_records['Total'].sum() * 100).round(2)

# Add a 'Total General' row
total_general_row = pd.DataFrame(pivot_table_all_records.sum()).T
total_general_row.index = ['Total General']
pivot_table_all_records = pd.concat([pivot_table_all_records, total_general_row])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Centrale pharmaceutique'")
st.write(pivot_table_all_records)
