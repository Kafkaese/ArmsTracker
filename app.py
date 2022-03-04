import streamlit as st

import geopandas
import plotly.express as px

import subprocess

et = subprocess.run(["ls"], capture_output=True)
st.write(et)

et = subprocess.run(["pwd"], capture_output=True)
st.write(et)

#subprocess.run(["cd data/geo && pwd"])


#world = geopandas.read_file('/data/geo/world.geojson')

#world.drop(columns = ['zoneName', 'countryKey'], inplace = True)

#world.explore()