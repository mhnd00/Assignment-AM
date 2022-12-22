import streamlit as st 
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu

st.set_page_config(
  page_title="Assignment"
)



playStore = pd.read_csv('assignment/googleplaystore.csv')
st.title('googleplay Application')
playStore['Price'] = playStore['Price'].str.replace('$', '')
playStore['Price'] = playStore['Price'].str.replace('Everyone', '0')
playStore['Reviews'] = playStore['Reviews'].str.replace('M', '')
playStore['Installs'] = playStore['Installs'].str.replace('+','')
playStore['Installs'] = playStore['Installs'].str.replace('Free','0')
playStore['Installs'] = playStore['Installs'].str.replace(',','')
playStore.drop(playStore[playStore['Rating'] == 19. ].index, inplace=True)
playStore.dropna(inplace=True)
playStore = playStore.astype({'Price':float,'Reviews':float,'Installs':float})
playStoreApp = st.selectbox("Select app Genre of the App", playStore['Genres'].unique())
st.write(playStoreApp)
plot_type = st.radio("select the plot type",['scatter','line','histogram','Bar'])
if plot_type == 'scatter':
  pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp]).mark_circle().encode(
    x = 'Reviews',
    y = 'Installs',
    tooltip = ['Reviews','Installs']
).interactive()
elif plot_type == 'histogram':
  pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp]).mark_bar().encode(
    x = 'Reviews',
    y = 'count()',
    tooltip = ['Reviews']
).interactive()
elif plot_type == 'Bar':
  pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp]).mark_bar().encode(
    x = 'Reviews',
    y = 'App',
    tooltip = ['Reviews','App']
).interactive()
else :
  pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp]).mark_line().encode(
    x = 'Reviews',
    y = 'Installs',
    tooltip = ['Reviews','Installs']
).interactive()
st.altair_chart(pl)
