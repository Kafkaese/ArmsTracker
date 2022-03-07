import streamlit as st

import geopandas
import plotly.express as px


world = geopandas.read_file('data/geo/world.geojson')

world.drop(columns = ['zoneName', 'countryKey'], inplace = True)

world.explore()

st.pyplot()
