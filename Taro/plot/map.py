from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
from bokeh.palettes import brewer

from bokeh.io.doc import curdoc
from bokeh.models import HoverTool
from bokeh.layouts import column

def plot_export_map(data, **kwargs):
    """
    Plots map with exports based on @data
    
    Parameters
    ----------
    data : GeoJSON, data with arms export data and country polygond
    """
    
    #convert GeoJSON to datasource
    geosource = GeoJSONDataSource(geojson = data)

    # pick palette
    palette = brewer['Blues'][8]
    palette = palette[::-1]
    
    # Create figure
    p = figure(title = 'Title', 
             plot_height = 700, plot_width = 1200,
             toolbar_location = None)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.axis.visible = False

    # Add patch renderer to figure. 
    p.patches('xs','ys', source = geosource,
          line_color = 'black', line_width = 0.25, fill_alpha = 1)

    # Specify color bar layout.
    #p.add_layout(color_bar, 'right')

    # Add hover tool
    hover = HoverTool(tooltips = [ ('Name','@countryName'), ('Total Exports 2020 (Million EUR)', '@total_mil')])

    # Add the hover tool to the graph
    p.add_tools(hover)
    
    layout = column(p)
    curdoc().add_root(layout)