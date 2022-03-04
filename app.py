import streamlit as st

import geopandas
import plotly.express as px

import subprocess
subprocess.run(["ls"])

import subprocess
subprocess.run(["pwd"])


import subprocess
subprocess.run(["cd data/geo && pwd"])


world = geopandas.read_file('/data/geo/world.geojson')

world.drop(columns = ['zoneName', 'countryKey'], inplace = True)

world.explore()