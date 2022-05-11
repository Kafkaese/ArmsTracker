import pandas as pd
import geopandas


from bokeh.layouts import column, row
from bokeh.client import push_session
from bokeh.io.doc import curdoc


from taro.preproc.plotting import get_plot_export_data, get_sidebar_export_data
from taro.plot import plot_export_map, plot_sidebar

print(__file__)


geo_data = geopandas.read_file('../data/geo/custom_world.json')



export_data = pd.read_csv('https://raw.githubusercontent.com/caatdata/eu-arms-export-data/master/export.csv', delimiter=';', header=None)

# drop empty column
#export_data = export_data.drop(columns = [11])
#export_data.columns = ['year', 'embargo', 'source_country', 'source_country_name', 'destination_country', 'destination_country_name', 'region_code', 'region_name', 'rating', 'category', 'value']



data= get_plot_export_data(export_data=export_data, geo_data=geo_data, years=2020)
sidebar_data = get_sidebar_export_data(export_data, 'GB', 2019)

map = plot_export_map(data)
side = plot_sidebar(sidebar_data)

c = column(side)
layout = row(c , map)
curdoc().add_root(layout)

session = push_session(curdoc())
session.show()
