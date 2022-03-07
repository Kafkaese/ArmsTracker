import pandas as pd
import geopandas

from taro.preproc.plotting import get_plot_export_data
from taro.plot.map import plot_export_map

geo_data = geopandas.read_file('https://raw.githubusercontent.com/electricitymap/electricitymap-contrib/master/web/geo/world.geojson')

export_data = pd.read_csv('https://raw.githubusercontent.com/caatdata/eu-arms-export-data/master/export.csv', delimiter=';', header=None)

# drop empty column
export_data = export_data.drop(columns = [11])
export_data.columns = ['year', 'embargo', 'source_country', 'source_country_name', 'destination_country', 'destination_country_name', 'region_code', 'region_name', 'rating', 'category', 'value']

data = get_plot_export_data(export_data=export_data, geo_data=geo_data, years=2020)

plot_export_map(data)