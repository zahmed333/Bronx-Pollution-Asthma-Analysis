#importing libraries
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.io as pio


# Loadiing and cleaning Air_Quality data
datA = pd.read_csv('data/Air_Quality.csv')
datA = datA.drop('Message', 1)

datA = datA[(datA['Name'] == 'Fine Particulate Matter (PM2.5)') |
   (datA['Name'] == 'Nitrogen Dioxide (NO2)') |
   (datA['Name'] == 'Ozone (O3)')|
   (datA['Name'] == 'Sulfur Dioxide (SO2)')]

datA['Start_Date'] = datA['Start_Date'].apply(pd.to_datetime)
datA['Start_Date'] = datA['Start_Date'].dt.year

datA.drop(['Time Period', 'Indicator ID', 'Unique ID'], axis=1)
datA= datA[(datA['Start_Date'] <=2015) & (datA['Start_Date'] >=2009)]
datA = datA.rename({'Start_Date': 'TimeFrame',
                          'Geo Place Name':'Location',
                          'Name': 'Pollutant',
                          'Data Value': 'Mean Pollutant Value'}, axis=1)

datA = datA.drop(columns=['Unique ID', 'Indicator ID', 'Measure', 'Time Period'])
datA = datA[datA['Geo Type Name'] == 'CD']


#Loading and cleaning Asthma_Emergency_Department_Visits data
visits = pd.read_csv('data/Asthma_Emergency_Department_Visits.csv')
visits = visits.rename({'Fips': 'Geo Join ID'}, axis=1)

visits = visits[(visits['Location'] != 'South Bronx') &
        (visits['Location'] != 'Bronx')   &
        (visits['Location'] != 'New York City')]

#Mapping GeoJoinID
visits['Geo Join ID'] = visits['Geo Join ID'].map(lambda x: x.lstrip('uhf'))
visits['Geo Join ID'] = visits['Geo Join ID'].astype(int)
visits= visits[(visits['TimeFrame'] <=2015) & (visits['TimeFrame'] >=2009)]
visits = visits.rename(columns={'Data': 'Asthma Emergency Dep. Visits'})

nycb = json.load(open('json/UHF42.json', 'r'))
Boro_map = {}
for feature in nycb['features']:
    feature['Borough'] = feature['properties']['BOROUGH']
    Boro_map[feature['properties']['GEOCODE']] = feature['Borough']
visits['Borough'] = visits['Geo Join ID'].map(Boro_map)


#filtering Data depending on borough parameter
def Boroughdata(Borough):
    nycb = json.load(open('json/neigh.json', 'r'))
    Boro_map = {}
    for feature in nycb['features']:
        feature['Borough'] = feature['properties']['BOROUGH']
        Boro_map[feature['properties']['GEOCODE']] = feature['Borough']
    datA['Borough'] = datA['Geo Join ID'].map(Boro_map)
    x = datA[datA['Borough'] == Borough]
    return x

#creating choropleth map for specific borough using filtered borough data
def Bmap(data):
    nycb = json.load(open('json/neigh.json', 'r'))
    fig = px.choropleth_mapbox(data, locations='Geo Join ID', geojson=nycb, color='Mean Pollutant Value', hover_name='Location', mapbox_style='carto-positron', center = {'lat':40.681395467965096, 'lon':-73.93646399798689}, zoom=9, opacity = 0.5)
    return fig

#creating a pie chart according input year and borough
def Piech(year, data, Borough):
    df = data.query("TimeFrame == {}".format(year))
    fig = px.pie(df, values='Mean Pollutant Value', names='Pollutant', title=Borough +' Pollutants in ' + year)
    return fig

#creating asthma choropleth map
def asthmamap(visits):
    nyc = json.load(open('json/boroughsgeojson.json', 'r'))
    Boro = {}
    y = visits.dropna()
    for feature in nyc['features']:
        feature['id'] = feature['properties']['BoroCode']
        Boro[feature['properties']['BoroName']] = feature['id']
    y['BoroughID'] = y['Borough'].apply(lambda x: Boro[x])

    location = 'Geo Join ID'
    geo = nycb
    hover = 'Location'
    fig = px.choropleth_mapbox(y, locations=location, geojson=geo, color='Asthma Emergency Dep. Visits', hover_name=hover, mapbox_style='carto-positron', center = {'lat':40.681395467965096, 'lon':-73.93646399798689}, zoom=8, opacity = 0.5)
    return fig

#creating pie chart for nyc pollutants
def nycpie():
    fig = px.pie(datA, values='Mean Pollutant Value', names='Pollutant', title='Pollutants in NYC')
    return fig
