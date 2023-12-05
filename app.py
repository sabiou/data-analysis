import streamlit as st
import pandas as pd
import altair as alt


file_path = "database.xlsx"
df = pd.read_excel(file_path)


st.write("## Displaying DataFrame")
st.write(df)

# Select the column to plot
column_to_plot = 'Pourcentage'

# Select the rows to plot (excluding the "Total générale" row)
rows_to_plot = df.index[:-1]

# Filter the DataFrame for the selected column and rows
data_to_plot = df.loc[rows_to_plot, column_to_plot].reset_index()

# Create an Altair chart
chart = alt.Chart(data_to_plot).mark_bar().encode(
    y=alt.Y('Centrales pharmaceutiques:N', sort='-x'),
    x=alt.X('Pourcentage:Q'),
    color=alt.Color('Pourcentage:Q', scale=alt.Scale(scheme='viridis')),
    tooltip=['Centrales pharmaceutiques:N', 'Pourcentage:Q']
).properties(
    width=600,
    height=400
)

# Display the Altair chart using Streamlit
st.write("## Altair Chart")
st.altair_chart(chart, use_container_width=True)
