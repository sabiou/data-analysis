import streamlit as st
import pandas as pd
import altair as alt
import locale


# Set the locale to French
locale.setlocale(locale.LC_NUMERIC, 'fr_FR.UTF-8')

file_path = "database.xlsx"
df = pd.read_excel(file_path)

# Filtrer les données pour la valeur "Centrale pharmaceutique" dans la colonne "Profil"
data_centrale = df[df['Profil'] == 'Centrale pharmaceutique']

# Création d'une table pivot pour les données de "Centrale pharmaceutique"
pivot_table_centrale = data_centrale.pivot_table(
    index='DEMANDEUR', 
    columns='ANNEE', 
    values='QUANTITE A COMMANDER( BOITES)', 
    aggfunc='sum', 
    fill_value=0
)

# Ajout d'une colonne Total
pivot_table_centrale['Total'] = pivot_table_centrale.sum(axis=1)

# Calcul du pourcentage global pour chaque ligne
pivot_table_centrale['Pourcentage'] = (pivot_table_centrale['Total'] / pivot_table_centrale['Total'].sum() * 100).round(3)

# Ajout de la ligne "Total générale"
total_generale_centrale = pd.DataFrame(pivot_table_centrale.sum()).T
total_generale_centrale.index = ['Total générale']
pivot_table_centrale = pd.concat([pivot_table_centrale, total_generale_centrale])

# Création d'un nouveau DataFrame avec le tableau de répartition pour "Centrale pharmaceutique"
tableau_repartition_centrale_df = pd.DataFrame(pivot_table_centrale[['Total', 'Pourcentage']])

# Renommer les colonnes pour le Streamlit
pivot_table_centrale = pivot_table_centrale.rename_axis(columns={'ANNEE': 'Centrales pharmaceutiques'})

# Affichage du tableau pivot pour "Centrale pharmaceutique"
st.write("## Pivot Table for 'Centrale pharmaceutique'")
st.write(pivot_table_centrale)
