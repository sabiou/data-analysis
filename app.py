import streamlit as st
import pandas as pd
import altair as alt
import locale
from io import StringIO


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
    index=['DEMANDEUR'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records['Total'] = pivot_table_all_records.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records['Percentage'] = (pivot_table_all_records['Total'] / pivot_table_all_records['Total'].sum() * 100).round(3)

# Add a 'Total General' row
total_general_row = pd.DataFrame(pivot_table_all_records.sum()).T
total_general_row.index = ['Total General']
pivot_table_all_records = pd.concat([pivot_table_all_records, total_general_row])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Centrale pharmaceutique'")
st.write(pivot_table_all_records)



# Filter the data for the value "Centrale pharmaceutique" in the "Profil" column
data_ong = df[df['Profil'] == 'ONG Internationale']

# Remove spaces from column names in data_ong
data_ong.columns = data_ong.columns.str.strip()

# Get unique DEMANDEUR values corresponding to ONG Internationale
demandeurs_ong = data_ong['DEMANDEUR'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to ONG Internationale in the DEMANDEUR column
df_ong_records = df[df['DEMANDEUR'].isin(demandeurs_ong)]

# Create a pivot table for the new DataFrame
pivot_table_all_records_ong = df_ong_records.pivot_table(
    index=['DEMANDEUR'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records_ong['Total'] = pivot_table_all_records_ong.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records_ong['Percentage'] = (pivot_table_all_records_ong['Total'] / pivot_table_all_records_ong['Total'].sum() * 100).round(3)

# Add a 'Total General' row
total_general_row_ong = pd.DataFrame(pivot_table_all_records_ong.sum()).T
total_general_row_ong.index = ['Total General']
pivot_table_all_records_ong = pd.concat([pivot_table_all_records_ong, total_general_row_ong])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'ONG Internationale'")
st.write(pivot_table_all_records_ong)




# Filter the data for the value "Centrale pharmaceutique" in the "Profil" column
data_ong = df[df['Profil'] == 'ONG Internationale']

# Remove spaces from column names in data_ong
data_ong.columns = data_ong.columns.str.strip()

# Get unique DEMANDEUR values corresponding to ONG Internationale
demandeurs_ong = data_ong['DEMANDEUR'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to ONG Internationale in the DEMANDEUR column
df_ong_records = df[df['DEMANDEUR'].isin(demandeurs_ong)]

# Create a pivot table for the new DataFrame
pivot_table_all_records_ong = df_ong_records.pivot_table(
    index=['DEMANDEUR'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records_ong['Total'] = pivot_table_all_records_ong.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records_ong['Percentage'] = (pivot_table_all_records_ong['Total'] / pivot_table_all_records_ong['Total'].sum() * 100).round(3)

# Add a 'Total General' row
total_general_row_ong = pd.DataFrame(pivot_table_all_records_ong.sum()).T
total_general_row_ong.index = ['Total General']
pivot_table_all_records_ong = pd.concat([pivot_table_all_records_ong, total_general_row_ong])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'ONG Internationale'")
st.write(pivot_table_all_records_ong)


# Filter the data for the value "Centrale pharmaceutique" in the "Profil" column
data_off = df[df['Profil'] == 'Officine']

# Get unique DEMANDEUR values corresponding to ONG Internationale
demandeurs_off = data_off['DEMANDEUR'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to ONG Internationale in the DEMANDEUR column
df_off_records = df[df['DEMANDEUR'].isin(demandeurs_off)]

# Create a pivot table for the new DataFrame
pivot_table_all_records_off = df_off_records.pivot_table(
    index=['DEMANDEUR'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records_off['Total'] = pivot_table_all_records_off.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records_off['Percentage'] = (pivot_table_all_records_off['Total'] / pivot_table_all_records_off['Total'].sum() * 100).round(3)

# Add a 'Total General' row
total_general_row_off = pd.DataFrame(pivot_table_all_records_off.sum()).T
total_general_row_off.index = ['Total General']
pivot_table_all_records_off = pd.concat([pivot_table_all_records_off, total_general_row_off])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Officine'")
st.write(pivot_table_all_records_off)

# Create a pivot table for Classes Therapeutiques
pivot_table_classes = df.pivot_table(
    index=['Classes Therapeutiques'],
    columns='ANNEE',
    values='QUANTITE A COMMANDER( BOITES)',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

# Calculate percentages for each cell
percentage_table_classes = (pivot_table_classes.div(pivot_table_classes.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_table_classes['Percentage'] = (pivot_table_classes['Total'] / pivot_table_classes['Total'].loc['Total'] * 100).round(2)

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for 'Classes Therapeutiques'")
st.write(pivot_table_classes.join(percentage_table_classes['Percentage']))



# 
data_dci = df[df['Classes Therapeutiques'] == 'Antalgiques/Analgésiques']

# Remove spaces from column names in data_ong
data_dci.columns = data_dci.columns.str.strip()

# Get unique DEMANDEUR values corresponding to ONG Internationale
dci = data_dci['DCI'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to ONG Internationale in the DEMANDEUR column
df_dci_records = df[df['DCI'].isin(dci)]

# Create a pivot table for the new DataFrame
pivot_table_all_records_dci = df_dci_records.pivot_table(
    index=['DCI'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records_dci['Total'] = pivot_table_all_records_dci.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records_dci['Percentage'] = (pivot_table_all_records_dci['Total'] / pivot_table_all_records_dci['Total'].sum() * 100).round(3)

# Add a 'Total General' row
total_general_row_dci = pd.DataFrame(pivot_table_all_records_dci.sum()).T
total_general_row_dci.index = ['Total General']
pivot_table_all_records_dci = pd.concat([pivot_table_all_records_dci, total_general_row_dci])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'DCI'")
st.write(pivot_table_all_records_dci)


# 
data_dci_anx = df[df['Classes Therapeutiques'] == 'Anxiolytiques']

# Remove spaces from column names in data_ong
data_dci_anx.columns = data_dci_anx.columns.str.strip()

# Get unique DEMANDEUR values corresponding to ONG Internationale
anx = data_dci_anx['DCI'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to ONG Internationale in the DEMANDEUR column
df_anx_records = df[df['DCI'].isin(anx)]

# Create a pivot table for the new DataFrame
pivot_table_all_records_anx = df_anx_records.pivot_table(
    index=['DCI'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records_anx['Total'] = pivot_table_all_records_anx.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records_anx['Percentage'] = (pivot_table_all_records_anx['Total'] / pivot_table_all_records_anx['Total'].sum() * 100).round(3)

# Add a 'Total General' row
total_general_row_anx = pd.DataFrame(pivot_table_all_records_anx.sum()).T
total_general_row_anx.index = ['Total General']
pivot_table_all_records_anx = pd.concat([pivot_table_all_records_anx, total_general_row_anx])

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Anxiolytiques'")
st.write(pivot_table_all_records_anx)
