import json
from flag import flag

def get_plot_export_data(export_data, geo_data, years):
    """
    Filters data based on @year and merges the two dataframes ready for the interactive map.
    
    Parameters
    ----------
    export_data : DataFram with arms export data per country
    geo_data : Polygons for world map plot
    year : int or list of int, the year(s) to be plotted
        
    Returns
    -------
    data : GeoJSON, ready for plotting in bokeh 
    """
    # Drop empty column
    export_data = export_data.drop(columns = [11]) 
    
    # Set column names
    export_data.columns = ['year', 'embargo', 'source_country', 'source_country_name', 'destination_country', 'destination_country_name', 'region_code', 'region_name', 'rating', 'category', 'value']
    
    # Remove missing source countries and target countries
    export_data = export_data[export_data['source_country'] != ' ']
    export_data = export_data[export_data['destination_country'] != ' ']
    
    
    # Filter for years
    if not isinstance(years, list):
        years = [years]
    
    # Filter export data by year and calculate yearly total
    export_total_data = export_data[export_data['year'].isin(years)].groupby('source_country')[['value']].sum()
    
    #return export_total_data
    export_total_data.reset_index(inplace = True)
    
    export_total_data['flag'] = export_total_data['source_country'].apply(flag)
    
    export_total_data.set_index('source_country')
    
    # Rename export data column to match geo data colums
    export_total_data = export_total_data.reset_index().rename(columns={'source_country': 'countryKey'})
    
    
    # Clean @countryKey in export data
    export_total_data['countryKey'] = export_total_data['countryKey'].apply(lambda x: x.strip())
    
    
    # Merge export with geo data
    data = geo_data.merge(export_total_data, how='left', on='countryKey')
    
    # Round value to millions
    data['total_mil'] = data['value'].apply(lambda x: round(x/1000000, 2))
    
    #data_raw = data
    
    # Convert to GeoJSON
    data = json.dumps(json.loads(data.to_json()))
    

    return data #, data_raw