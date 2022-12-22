import altair as alt
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
alt.data_transformers.disable_max_rows()
st.title('Data Analized')
st.write('Pie plot of a sample data of 10 apps and their price')

playStore = pd.read_csv('assignment/googleplaystore.csv')
playStore['Price'] = playStore['Price'].str.replace('$', '')
playStore['Price'] = playStore['Price'].str.replace('Everyone', '0')
playStore['Reviews'] = playStore['Reviews'].str.replace('M', '')
playStore = playStore.astype({'Price':float,'Reviews':float})
playStore.drop(playStore[playStore['Rating'] == 19. ].index, inplace=True)
playStore.dropna(inplace=True)
sampledata  = playStore.head(10).copy()


st.subheader("Bar chart shows geners of apps and Rating for sample of 10 apps")
st.bar_chart(data=sampledata.head(40), x='App', y='Rating', width=400, height=400, use_container_width=True)
st.subheader("Area chart")
st.area_chart(data=sampledata, x='Installs', y='Reviews', width=0, height=0, use_container_width=True,)
st.spinner()
