"""Visualization utilities for EV charging station data."""

import folium
from typing import List
from folium import plugins
from ..models.data_models import ChargingStation

def create_station_map(stations: List[ChargingStation], city: str, state: str) -> folium.Map:
    """
    Create an interactive map showing EV charging stations.
    
    Args:
        stations: List of ChargingStation objects
        city: City name
        state: State name
        
    Returns:
        Folium map object
    """
    # Calculate center point (average of all stations)
    if not stations:
        raise ValueError("No stations provided for map visualization")
        
    center_lat = sum(station.latitude for station in stations) / len(stations)
    center_lon = sum(station.longitude for station in stations) / len(stations)
    
    # Create the map with a modern tile layer
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12,
        tiles='CartoDB positron',
        width='100%',
        height='100%'
    )
    
    # Add a fullscreen button
    plugins.Fullscreen().add_to(m)
    
    # Create a MarkerCluster for better performance with many markers
    marker_cluster = plugins.MarkerCluster().add_to(m)
    
    # Add markers for each station
    for station in stations:
        # Create detailed popup content
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; min-width: 200px;">
            <h4 style="margin: 0 0 10px 0;">{station.name}</h4>
            <p style="margin: 5px 0;"><b>Address:</b> {station.address}</p>
            <p style="margin: 5px 0;"><b>Status:</b> {station.status}</p>
            <p style="margin: 5px 0;"><b>Access:</b> {station.access_type}</p>
            <p style="margin: 5px 0;"><b>Network:</b> {station.network or 'N/A'}</p>
            <p style="margin: 5px 0;"><b>Connectors:</b> {', '.join(station.connector_types)}</p>
            <p style="margin: 5px 0;"><b>Hours:</b> {station.hours or 'N/A'}</p>
            <p style="margin: 5px 0;"><b>Pricing:</b> {station.pricing or 'N/A'}</p>
        </div>
        """
        
        # Determine marker color based on status
        if station.status.lower() == "e":  # Available
            icon_color = "green"
        elif station.status.lower() == "p":  # Planned
            icon_color = "orange"
        else:  # Not available or unknown
            icon_color = "red"
            
        # Create marker with custom icon and popup
        folium.Marker(
            location=[station.latitude, station.longitude],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(
                color=icon_color,
                icon='plug',
                prefix='fa'
            )
        ).add_to(marker_cluster)
    
    # Add a title
    title_html = f'''
        <div style="position: fixed; 
                    top: 10px; 
                    left: 50px; 
                    width: 300px; 
                    height: 60px; 
                    z-index: 1000;
                    background-color: white;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);">
            <h3 style="margin: 0; text-align: center;">
                EV Charging Stations<br>
                {city}, {state}
            </h3>
        </div>
    '''
    m.get_root().html.add_child(folium.Element(title_html))
    
    # Add a legend
    legend_html = '''
        <div style="position: fixed; 
                    bottom: 50px; 
                    right: 50px; 
                    width: 150px;
                    height: 100px; 
                    z-index: 1000;
                    background-color: white;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);">
            <h4 style="margin: 0 0 10px 0;">Status</h4>
            <p style="margin: 5px 0;">
                <i class="fa fa-circle" style="color: green;"></i> Available
            </p>
            <p style="margin: 5px 0;">
                <i class="fa fa-circle" style="color: orange;"></i> Planned
            </p>
            <p style="margin: 5px 0;">
                <i class="fa fa-circle" style="color: red;"></i> Not Available
            </p>
        </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    return m
