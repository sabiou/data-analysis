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
percentage_table['Percentage'] = (pivot_table['Total'] / pivot_table['Total'].loc['Total'] * 100).round(3)

# Display the pivot table with original values and percentage using Streamlit
st.write("## Pivot Table")
st.write(pivot_table.join(percentage_table['Percentage']))

# Create an Altair chart for visualization
melted_table = pd.melt(pivot_table.reset_index(), id_vars='Profil', var_name='Year', value_name='Quantity')
chart = alt.Chart(melted_table).mark_bar().encode(
    x='Year:N',
    y='Quantity:Q',
    color='Profil:N',
    tooltip=['Profil:N', 'Year:N', 'Quantity:Q']
).properties(
    width=600,
    height=400
)

# Display the Altair chart using Streamlit
st.write("## Altair Chart")
st.altair_chart(chart, use_container_width=True)
