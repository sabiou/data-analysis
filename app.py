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

# Add a 'Percentage' column for each 'Profil'
percentage_table['Percentage'] = (percentage_table['Total'] / percentage_table['Total'].sum() * 100).round(2)

# Display the pivot table using Streamlit
st.write("## Pivot Table")
st.write(percentage_table)

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
