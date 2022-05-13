import streamlit as st
import Analysis
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import altair as alt
from PIL import Image


#setting up page configurations

st.set_page_config(
     page_title="Data Visualization of NYC and The Bronx",
     page_icon="chart_with_upwards_trend",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

title = '<p style="font-family:Roboto, sans-serif; color:#5184AA; font-size: 22px;">Air pollution in The Bronx and NYC emergency visits</p>'
sidebarTitle = '<p style="font-family:Roboto, sans-serif; color:#465fab; font-size: 22px;">Data</p>'
FPM = '<p style="font-family:Roboto, sans-serif; color:#5184AA; font-size: 15px;">Fine Particulate Matter (PM2.5) :  Fine particles are released by automobiles, building boilers, and other forms of combustion, and are a major source of air pollution that impacts human health.</p>'
ND = '<p style="font-family:Roboto, sans-serif; color:#5184AA; font-size: 15px;">Nitrogen Dioxide (NO2): is a type of pollutant produced by combustion that can harm lung tissue, induce breathing and respiratory issues, and contribute to smog and acid rain.</p>'
SD= '<p style="font-family:Roboto, sans-serif; color:#5184AA; font-size: 15px;">Sulfur Dioxide (SO2):  Sulfur dioxide comes from burning certain types of fuel oil. As an air pollutant, it can can worsen lung diseases. </p>'
OZ= '<p style="font-family:Roboto, sans-serif; color:#5184AA; font-size: 15px;">Ozone (O3):  Ozone is a common air pollutant that can harm breathing and worsen asthma and other respiratory conditions.</p>'
poll= '<p style="font-family:Roboto, sans-serif; color:#465fab; font-size: 20;">Pollutants</p>'
st.title('Air pollution in the Bronx')
st.sidebar.markdown(sidebarTitle, unsafe_allow_html=True)
st.markdown(title, unsafe_allow_html=True)
pollimg = Image.open('images/pollution.png')

st.image(pollimg, width = 400)

Borough = st.sidebar.selectbox(
    "NYC is for Emergency visits and Bronx is for Mean pollutants",
    ("New York City", "Bronx")
)

st.sidebar.markdown(poll, unsafe_allow_html=True)
st.sidebar.markdown(FPM, unsafe_allow_html=True)
st.sidebar.markdown(ND, unsafe_allow_html=True)
st.sidebar.markdown(SD, unsafe_allow_html=True)
st.sidebar.markdown(OZ, unsafe_allow_html=True)

#Loading Image
image = Image.open('images/Lung.png')
st.sidebar.image(image)

st.write('The emergency visits regarding asthma from 2009 to 2015 in NYC and The Bronx. The average of pollutants in the air are analyzed— the ones analyzed are on the right.\n A map is created for mapping GIS data and visualized with intensity of color. Furthermore, there is one with emergency visits, and another with mean pollutant value. Finally, the last chart is a pie chart over 6 years.')


if Borough == "New York City":
    df = Analysis.visits
    st.code('import pandas as pd\nvisits = pd.read_csv(\'Asthma_Emergency_Department_Visits.csv\')')
    st.write(Borough + ' Data')

    #displaying dataframe on page
    st.dataframe(df.head(50))
    st.write('\nDisplaying choropleth map of asthma emergency department visits in NYC areas from year 2009-2015')
    fig = Analysis.asthmamap(df)

    st.write(fig)
    pie = Analysis.nycpie()
    st.write(pie)
else:
    df = Analysis.Boroughdata(Borough)
    st.code('import pandas as pd\ndatA = pd.read_csv(\'Air_Quality.csv\')')
    st.write(Borough + ' Data')
    st.dataframe(df.head(50))

    st.write('Map of Pollution values in ' + Borough + ' according to area: ')
    borough_map = Analysis.Bmap(df)
    st.write(borough_map)

    select_year = '<p style="font-family:Palatino, URW Palladio L, serif; color:#0E715F; font-size: 22px;">Select Year</p>'
    st.markdown(select_year, unsafe_allow_html=True)

    Year = st.slider("Year",min_value= 2009, max_value = 2015, step = 1)
    fig = Analysis.Piech(str(Year), df, Borough)
    st.write(fig)


dataused = '<p style="font-family:Palatino, URW Palladio L, serif; color:#465fab; font-size: 14px;">Data Citation:</p>'
st.markdown(dataused, unsafe_allow_html=True)
st.write('[Air Quality Data from NYC Open Data](https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r)')
st.write('[Asthma Emergency Department Visits from Citizen’s Committee for children of New York](https://data.cccnewyork.org/data/table/6/asthma-emergency-department-visits#6/9/22/a/a)')

dataused = '<p style="font-family:Palatino, URW Palladio L, serif; color:#465fab; font-size: 14px;">Image Citation:</p>'
st.markdown(dataused, unsafe_allow_html=True)
st.write('[Top City Image](https://www.nytimes.com/2012/06/10/realestate/the-hub-the-bronx-living-in-people-shops-and-roads-converge-here.html)')
st.write('[Sidebar infographic](https://ecolink.com/info/six-common-air-pollutants/)')
