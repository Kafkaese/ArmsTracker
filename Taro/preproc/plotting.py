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
    data : DataFrame, ready for plotting in bokeh 
    """
    
    if not isinstance(years, list):
        yeasr = [years]
    
    # Filter export data by year and calculate yearly total
    export_total_data = export_data[export_data['year'].isnin(years)].groupby('source_country')[['value']].sum()
    
    # Rename export data column to match geo data colums
    export_total_data = export_total_data.reset_index().rename(columns={'source_country': 'countryKey'})
    
    # Clean @countryKey in export data
    export_total_data['countryKey'] = export_total_data['countryKey'].apply(lambda x: x.strip())
    
    # Merge export with geo data
    data = geo_data.merge(export_total_data, how='left', on='countryKey')
    
    # Round value to millions
    data['total_mil'] = data['value'].apply(lambda x: round(x/1000000, 2))
    
    return data