import streamlit as st
import pandas as pd
import altair as alt
import locale
from io import StringIO

# Custom formatting function to remove the '%' sign
def remove_percent_sign(value):
    if isinstance(value, str) and value.endswith('%'):
        return value[:-1]
    return value


# Set the locale to French
locale.setlocale(locale.LC_NUMERIC, 'fr_FR.UTF-8')

file_path = "database.xlsx"
df = pd.read_excel(file_path)


# Create a pivot table
pivot_table = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['Profil'],
    columns=['ANNEE'],
    aggfunc={'QUANTITE A COMMANDER( BOITES)': 'sum'},
    margins=True,
    margins_name='Total',
    fill_value=0,
)


# Calculate percentages for each cell
percentage_table = (pivot_table.div(pivot_table.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_table['Pourcentage'] = (pivot_table['Total'] / pivot_table['Total'].loc['Total'] * 100).round(2)


# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table.join(percentage_table['Pourcentage']).style.format(thousands="", precision=2, decimal=","))


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
pivot_table_all_records['Pourcentage'] = (pivot_table_all_records['Total'] / pivot_table_all_records['Total'].sum())

# Add a 'Total General' row
total_general_row = pd.DataFrame(pivot_table_all_records.sum()).T
total_general_row.index = ['Total General']
pivot_table_all_records = pd.concat([pivot_table_all_records, total_general_row])

pivot_table_all_records = pivot_table_all_records.rename_axis("Centrales")

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Centrale pharmaceutique'")
st.write(pivot_table_all_records.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))


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
pivot_table_all_records_ong['Pourcentage'] = (pivot_table_all_records_ong['Total'] / pivot_table_all_records_ong['Total'].sum())

# Add a 'Total General' row
total_general_row_ong = pd.DataFrame(pivot_table_all_records_ong.sum()).T
total_general_row_ong.index = ['Total General']
pivot_table_all_records_ong = pd.concat([pivot_table_all_records_ong, total_general_row_ong])

pivot_table_all_records_ong = pivot_table_all_records_ong.rename_axis("ONG")

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'ONG Internationale'")
st.write(pivot_table_all_records_ong.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))

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
pivot_table_all_records_off['Pourcentage'] = (pivot_table_all_records_off['Total'] / pivot_table_all_records_off['Total'].sum())

# Add a 'Total General' row
total_general_row_off = pd.DataFrame(pivot_table_all_records_off.sum()).T
total_general_row_off.index = ['Total General']
pivot_table_all_records_off = pd.concat([pivot_table_all_records_off, total_general_row_off])

pivot_table_all_records_off = pivot_table_all_records_off.rename_axis("Officines")

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Officine'")
st.write(pivot_table_all_records_off.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))

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
percentage_table_classes['Pourcentage'] = (pivot_table_classes['Total'] / pivot_table_classes['Total'].loc['Total'] * 100).round(2)

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for 'Classes Therapeutiques'")
st.write(pivot_table_classes.join(percentage_table_classes['Pourcentage']).style.format(thousands="", precision=2, decimal=","))


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
pivot_table_all_records_dci['Pourcentage'] = (pivot_table_all_records_dci['Total'] / pivot_table_all_records_dci['Total'].sum())

# Add a 'Total General' row
total_general_row_dci = pd.DataFrame(pivot_table_all_records_dci.sum()).T
total_general_row_dci.index = ['Total General']
pivot_table_all_records_dci = pd.concat([pivot_table_all_records_dci, total_general_row_dci])

pivot_table_all_records_dci = pivot_table_all_records_dci.rename_axis("DCI")

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Antalgiques/Analgésiques'")
st.write(pivot_table_all_records_dci.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))


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
pivot_table_all_records_anx['Pourcentage'] = (pivot_table_all_records_anx['Total'] / pivot_table_all_records_anx['Total'].sum())

# Add a 'Total General' row
total_general_row_anx = pd.DataFrame(pivot_table_all_records_anx.sum()).T
total_general_row_anx.index = ['Total General']
pivot_table_all_records_anx = pd.concat([pivot_table_all_records_anx, total_general_row_anx])

pivot_table_all_records_anx = pivot_table_all_records_anx.rename_axis("DCI")

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Anxiolytiques'")
st.write(pivot_table_all_records_anx.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))


# 
data_dci_antiep = df[df['Classes Therapeutiques'] == 'Antiepileptiques']

# Remove spaces from column names in data_ong
data_dci_antiep.columns = data_dci_antiep.columns.str.strip()

# Get unique DEMANDEUR values corresponding to ONG Internationale
antiep = data_dci_antiep['DCI'].unique()

# Remove spaces from column names in the original DataFrame
df.columns = df.columns.str.strip()

# Create a new DataFrame with records corresponding to ONG Internationale in the DEMANDEUR column
df_antiep_records = df[df['DCI'].isin(antiep)]

# Create a pivot table for the new DataFrame
pivot_table_all_records_antiep = df_antiep_records.pivot_table(
    index=['DCI'],
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Add a 'Total' column
pivot_table_all_records_antiep['Total'] = pivot_table_all_records_antiep.sum(axis=1)

# Calculate the percentage for each row
pivot_table_all_records_antiep['Pourcentage'] = (pivot_table_all_records_antiep['Total'] / pivot_table_all_records_antiep['Total'].sum())

# Add a 'Total General' row
total_general_row_antiep = pd.DataFrame(pivot_table_all_records_antiep.sum()).T
total_general_row_antiep.index = ['Total General']
pivot_table_all_records_antiep = pd.concat([pivot_table_all_records_antiep, total_general_row_antiep])

pivot_table_all_records_antiep = pivot_table_all_records_antiep.rename_axis("DCI")

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for All Records Corresponding to 'Antiepileptiques'")
st.write(pivot_table_all_records_antiep.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))


# Create a pivot table for PAYS DE PROVENANCE
pivot_table_pays = df.pivot_table(
    index=['PAYS DE PROVENANCE'],
    columns='ANNEE',
    values='QUANTITE A COMMANDER( BOITES)',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

# Calculate percentages for each cell
percentage_table_pays = (pivot_table_pays.div(pivot_table_pays.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_table_pays['Pourcentage'] = (pivot_table_pays['Total'] / pivot_table_pays['Total'].loc['Total'] * 100).round(2)

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for 'PAYS DE PROVENANCE'")
st.write(pivot_table_pays.join(percentage_table_pays['Pourcentage']).style.format(thousands="", precision=2, decimal=","))


# Remove spaces from column names
df.columns = df.columns.str.strip()

# Create a pivot table for FORME PHARMACEUTIQUE
pivot_table_formes = df.pivot_table(
    index=['FORME PHARMACEUTIQUE'],
    columns='ANNEE',
    values='QUANTITE A COMMANDER( BOITES)',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

# Calculate percentages for each cell
percentage_table_formes = (pivot_table_formes.div(pivot_table_formes.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_table_formes['Pourcentage'] = (pivot_table_formes['Total'] / pivot_table_formes['Total'].loc['Total'] * 100).round(2)

pivot_table_formes = pivot_table_formes[pivot_table_formes.index != 'comprimé']

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table for 'FORME PHARMACEUTIQUE'")
st.write(pivot_table_formes.join(percentage_table_formes['Pourcentage']).style.format(thousands="", precision=2, decimal=","))


# Remove spaces from column names
df.columns = df.columns.str.strip()

# Create a pivot table for Profile and FORME PHARMACEUTIQUE
pivot_table_profile_forme = df.pivot_table(
    index=['Profil'],
    columns='FORME PHARMACEUTIQUE',
    values='QUANTITE A COMMANDER( BOITES)',
    aggfunc='sum',
    fill_value=0
)

# Drop the 'Comprimé' column from the pivot table
pivot_table_profile_forme = pivot_table_profile_forme.drop(columns='comprimé')

# Update the 'Total' column
pivot_table_profile_forme['Total'] = pivot_table_profile_forme.sum(axis=1)

# Recalculate the percentage for each row
pivot_table_profile_forme['Pourcentage'] = (pivot_table_profile_forme['Total'] / pivot_table_profile_forme['Total'].sum())

# Add a 'Total General' row to the DataFrame
total_general_row = pd.DataFrame(pivot_table_profile_forme.sum()).T
total_general_row.index = ['Total générale']
updated_frame = pd.concat([pivot_table_profile_forme, total_general_row])

updated_frame = updated_frame.rename_axis("Profils / Formes")

# Display the updated DataFrame
st.write("## Updated DataFrame with 'Total General'")
st.write(updated_frame.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))

####

# Create a pivot table
pivot_table = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['ANNEE'],
    aggfunc='sum',
    margins=True,
    margins_name='Total générale'
)

# Calculate percentages for each cell
percentage_table = (pivot_table.div(pivot_table.iloc[-1, 0], axis=1) * 100).round(2)

# Rename columns
pivot_table.columns = ['Total']
percentage_table.columns = ['Pourcentage']

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table.join(percentage_table, rsuffix='_Pourcentage').style.format(thousands="", precision=2, decimal=","))

######

# Create a pivot table for Profile and FORME PHARMACEUTIQUE
pivot_table_profile_classe= df.pivot_table(
    index=['Classes Therapeutiques'],
    columns='FORME PHARMACEUTIQUE',
    values='QUANTITE A COMMANDER( BOITES)',
    aggfunc='sum',
    fill_value=0
)

pivot_table_profile_classe = pivot_table_profile_classe.drop(columns=['comprimé'], errors='ignore')

# Update the 'Total' column
pivot_table_profile_classe['Total'] = pivot_table_profile_classe.sum(axis=1)

# Recalculate the percentage for each row
pivot_table_profile_classe['Pourcentage'] = (pivot_table_profile_classe['Total'] / pivot_table_profile_classe['Total'].sum())

# Add a 'Total General' row to the DataFrame
total_general_row_c = pd.DataFrame(pivot_table_profile_classe.sum()).T
total_general_row_c.index = ['Total générale']
updated_frame_classe = pd.concat([pivot_table_profile_classe, total_general_row_c])

updated_frame_classe = updated_frame_classe.rename_axis("Classes / Formes")

# Display the updated DataFrame
st.write("## Updated DataFrame with 'Total General'")
st.write(updated_frame_classe.style.format(thousands="", precision=0, decimal=",", formatter={'Pourcentage': lambda x: remove_percent_sign(f"{x:.2%}")}))

### 

pivot_table_cont = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['CONTINENT'],
    columns=['ANNEE'],
    aggfunc={'QUANTITE A COMMANDER( BOITES)': 'sum'},
    margins=True,
    margins_name='Total'
)

# Calculate percentages for each cell
percentage_cont = (pivot_table_cont.div(pivot_table_cont.loc[:, 'Total'], axis=0) * 100).round(2)

# Add a 'Percentage' column
percentage_cont['Pourcentage'] = (pivot_table_cont['Total'] / pivot_table_cont['Total'].loc['Total'] * 100).round(2)

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table_cont.join(percentage_cont['Pourcentage']).style.format(thousands="", precision=2, decimal=","))


####
# Create pivot table
pivot_table_vd = pd.pivot_table(
    df,
    values='QUANTITE TOTAL A IMPORTER( MG)',
    index=['VOIE D\'ADMINISTRATION'],
    aggfunc={'QUANTITE TOTAL A IMPORTER( MG)': 'sum'},
    margins=True,
    margins_name='Total Générale'
)

# Calculate percentages for each row
percentage_vd = (pivot_table_vd / pivot_table_vd.loc['Total Générale', 'QUANTITE TOTAL A IMPORTER( MG)'] * 100).round(2)

# Add a 'Pourcentage' column to the pivot table
pivot_table_vd['Pourcentage'] = percentage_vd['QUANTITE TOTAL A IMPORTER( MG)']

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table_vd.style.format(thousands="", precision=2, decimal=","))

###


####
# Create pivot table
pivot_table_vd_b = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['VOIE D\'ADMINISTRATION'],
    aggfunc={'QUANTITE A COMMANDER( BOITES)': 'sum'},
    margins=True,
    margins_name='Total Générale'
)

# Calculate percentages for each row
percentage_vd_b = (pivot_table_vd_b / pivot_table_vd_b.loc['Total Générale', 'QUANTITE A COMMANDER( BOITES)'] * 100).round(2)

# Add a 'Pourcentage' column to the pivot table
pivot_table_vd_b['Pourcentage'] = percentage_vd_b['QUANTITE A COMMANDER( BOITES)']

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table_vd_b.style.format(thousands="", precision=2, decimal=","))

####



# Create pivot table
pivot_table_vd_b = pd.pivot_table(
    df,
    values='QUANTITE A COMMANDER( BOITES)',
    index=['VOIE D\'ADMINISTRATION'],
    aggfunc={'QUANTITE A COMMANDER( BOITES)': 'sum'},
    margins=True,
    margins_name='Total Générale'
)

# Calculate percentages for each row
percentage_vd_b = (pivot_table_vd_b / pivot_table_vd_b.loc['Total Générale', 'QUANTITE A COMMANDER( BOITES)'] * 100).round(2)

# Add a 'Pourcentage' column to the pivot table
pivot_table_vd_b['Pourcentage'] = percentage_vd_b['QUANTITE A COMMANDER( BOITES)']

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table_vd_b.style.format(thousands="", precision=2, decimal=","))


#####


# Création d'une table pivot avec comme index la colonne "DCI" et les colonnes "ANNEE"
pivot_table = df.pivot_table(index='DCI', columns='ANNEE', values='TENEUR TOTALE(BASE ANHYDRE)/GRS', aggfunc='sum', fill_value=0)

# Ajout d'une colonne "Total général"
pivot_table['Total général'] = pivot_table.sum(axis=1)

# Calcul du pourcentage global pour chaque ligne
pivot_table['Pourcentage'] = (pivot_table['Total général'] / pivot_table['Total général'].sum() * 100).round(2)

# Création d'un nouveau DataFrame avec le tableau de répartition
tableau_repartition_df = pd.DataFrame(pivot_table[['Total général', 'Pourcentage']])

pivot_table_sorted = pivot_table.sort_values(by='Pourcentage', ascending=False)

# Sélectionner les 6 premiers
top_10 = pivot_table_sorted.head(10)

# Display the pivot table using Streamlit
st.write("## Pivot Table")
st.write(top_10.style.format(thousands="", precision=2, decimal=","))

##
# Assuming df is your DataFrame with the given columns
# Replace this with your actual DataFrame
# df = ...

# Group by 'ANNEE' and get records for each year
records_by_year = [df[df['ANNEE'] == year] for year in df['ANNEE'].unique()]

# Display records for each year
records_table = pd.DataFrame({'Year': df['ANNEE'].unique(), 'Record Count': [records.shape[0] for records in records_by_year]})

# Append a new row "Total" to the dataframe with the sum of the values in "Record count" column
records_table.loc[len(records_table)] = ['Total', records_table['Record Count'].sum()]

# Calculate the percentage of each entry
records_table['Percentage'] = (records_table['Record Count'] / records_table['Record Count'].sum() * 100).round(2) * 2

# Display the updated table
st.write("## Records by Year with Percentage")
st.write(records_table)

####

# Create a bar chart
bars = alt.Chart(records_table[:-1]).mark_bar().encode(
    x='Year:O',
    y='Record Count:Q',
)

# Create a text chart for labels
text = bars.mark_text(
    align='center',
    baseline='bottom',
).encode(
    text='Record Count:Q'
)

# Display the chart with labels
st.altair_chart(bars + text)
