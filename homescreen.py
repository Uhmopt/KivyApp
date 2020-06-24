from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty, StringProperty
import webview
import time
import folium 
import os
import json
import requests
import altair as alt
import pandas as pd
import numpy as np

# folium map draw
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
vis1 = json.loads(requests.get(f'{url}/vis1.json').text)
vis2 = json.loads(requests.get(f'{url}/vis2.json').text)
vis3 = json.loads(requests.get(f'{url}/vis3.json').text)

# import pandas as pds
class HomeScreen(Screen):
    m = folium.Map(location = [52.1326, 5.2913], zoom_start = 5, title = 'Mt. Hood Meadows') 
    # CircleMarker with radius 
    folium.Marker(
        location=[52.1326, 5.2913],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis1, width=450, height=250)),
        icon=folium.Icon(color='red')
    ).add_to(m)
    folium.Marker( 
        location=[50.851368, 5.690973],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis2, width=450, height=250)),
        icon=folium.Icon(color='green') 
    ).add_to(m)

    folium.Marker(
        location=[52.518536, 5.471422], 
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis3, width=450, height=250)),
        icon=folium.Icon(color='red', icon='info-sign') 
    ).add_to(m)
    folium.Marker( 
        location=[52.785805, 6.897585], 
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis3, width=450, height=250)),
        icon=folium.Icon(color='red', icon='info-sign') 
    ).add_to(m)
    m.save('map.html')

    # altair chart draw
    
    np.random.seed(42)
    source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
                        columns=['A', 'B', 'C'], index=pd.RangeIndex(100, name='x'))
    source = source.reset_index().melt('x', var_name='category', value_name='y')

    # Create a selection that chooses the nearest point & selects based on x-value
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
        fields=['x'], empty='none')

    # The basic line
    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x='x:Q',
        y='y:Q',
        color='category:N'
    )

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(source).mark_point().encode(
        x='x:Q',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'y:Q', alt.value(' '))
    )

    # Draw a rule at the location of the selection
    rules = alt.Chart(source).mark_rule(color='gray').encode(
        x='x:Q',
    ).transform_filter(
        nearest
    )

    # Put the five layers into a chart and bind the data
    m = alt.layer(
        line, selectors, points, rules, text
    )
    m.save('chart.html')

    flag = BooleanProperty(False)
    def windowdraw(self):
        self.flag = True
        if self.flag:
            webview.create_window('Altair/VegaLite Markers', './map.html')
            webview.start()
    def chartwindow(self):
        self.flag = True
        if self.flag:
            webview.create_window('multiline_tooltip', './chart.html')
            webview.start()

    
   