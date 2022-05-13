Asthma and Air Pollutants in The Bronx							

Asthma and Air Pollutants in The Bronx

Zulnorain Ahmed

Colgate University

GEOG331: Environmental Data Science - Professor Loranty


# Introduction
# **Research question**
How does air pollution in the Bronx affect asthma rates of its citizens?
# **Description of topic**
`	`The Bronx is known for some of the most air polluted areas in New York City. It is home to 1.4 million people, and a 78% minority population. Furthermore, people here are the least affluent with a median income of 22k. (U.S. Census Bureau, 2020) Asthma is especially prevalent there, which affects all ages of people, diminishing their quality of life. It has double the death rate when comparing The Bronx, and New York City. (Maantay, Juliana. 2007) Air pollution is directly connected to the amount of cases for asthma as forms of air pollution cause it. One of the many forms that pollution takes is proximity to traffic-exposure from automobiles. (Spira et al 2011)

`	`In this paper, I will be investigating the different areas of the Bronx and their level of air pollutants between 2009 and 2015. Then, I will individually analyze 2014 from a separate dataset. Investigating the data will let me know where, when, and why air pollutants have occurred. It helps that I have lived in the Bronx for over 15 years, which further allows me to understand and analyze the urban landscape. I will do this by providing anecdotal evidence of certain areas’ reputation as a person who has interacted with the areas. This will allow me to assess which parts of the city are more polluted, and from there I can look into the health differences observed in the areas most affected. More specifically, I will be looking for a correlation between hospitalization rates and pollutant levels within neighborhoods. This correlation will be the main guideline for this paper, along with some supplemental information and analysis made.

**Background**

The main pollutants that I plan to talk about in this paper include: PM2.5 (Fine Particulate Matter), NO2 (Nitrogen Dioxide), SO2 (Sulfur Dioxide), and Ozone (O3). To provide some background, particulate matter the 2.5 stands for how many microns it can variate between in terms of size. You can think of this as air particles that consist of any liquid or solid substance. Fireplaces, car engines, and coal- or natural gas–fired power plants are all major PM 2.5 sources. (*The Particulars of PM 2.5*, 2014) It is generally considered a great harm to human lungs. (Takizawa, 2015). Nitrogen Dioxide comes from combustion as well. One common occurrence of it is burning a gas stove. (Warman, 2009) Sulfur Dioxide is something that comes from burning of fuel sources such as coal and diesel. (*Sulfur Dioxide*, 2020) Ozone is something you may see often if you live in a city. It develops in the atmosphere from gasses that come out of tailpipes, smokestacks and many other sources. High ozone levels contribute to haze or smog and can reduce lung function by making it difficult to breathe deeply. (*Air Pollution and Asthma | AAFA.org*, 2015)

**Proposed analysis**

I will extract air pollution data of the pollutants aforementioned for the neighborhoods within the Bronx. This data will consist of GIS data used from the United Hospital Fund. I will also use the Neighborhood Tabular Area (NTA) GIS data to create choropleth maps. Analyzing the pollutants aforementioned, These results will be combined as the same period and district for the asthma results, and then compare rates to see if there is a positive correlation between high pollutant levels and heightened rates of Asthma reports and possibly other health deficiencies. One temporal concern is that I expect air quality and asthma to be delayed since it takes time for low air quality to have an affect on the human body, there could be lags. However, since I am analyzing this data over such a large period of time, then we don’t have to worry about it too much, but something we must take into consideration.
# Methods
**Python Data and Analysis**

The primary datasets I will be using are provided by New York City. More specifically, I will be using NYC Open Data. The other one is the Citizens Committee of Children of New York City who provide data for asthma emergency department visits. This portal contains a data set for Air Quality for all of NYC. The packages I am importing are plotly, pandas, numpy, and json. I will subset this data into only Bronx data. Their data variable is what I will use to plot my different pollutants. I am then calculating the mean of all pollutants to visualize on a choropleth map of The Bronx. I will do this by selecting neighborhoods and analyzing IDs related to the average of multiple air pollutants. I will format different districts by GIS data used from the United Hospital Fund. I will make the same map for asthma emergency department visits. The date range I am analyzing is 2009-2015. For those years I will also calculate what percentage of pollutants in all of the Bronx. I will mainly use this as supplemental data to the R data. It is important to note that python pollutant measurements are made in mcg per cubic meter. The main reason for using python in this analysis was to be able to host the data on a website that makes it easily accessible. Using the link provided below you can view the scalable data at whichever year you want to observe. This was hosted using streamlit as the front-end of the site, which allows for free hosting and dataset viewing directly from the csv files that we analyze.

**Website Link**

<https://share.streamlit.io/zahmed333/bronx-pollution-asthma-analysis/main/streamlitapp.py> 

**R Data and Analysis**

The primary datasets I will be using are also provided by New York City. For analyzing, I am using NYC NTA (Neighborhood Tabular Areas) from the neighborhood health atlas containing values from 2014. It also provides me with every variable I need. The main data I am analyzing and comparing is preventable asthma hospitalizations. This is important because this data represents hospitalizations that could have been prevented if the person went to their primary care physician first. A choropleth map will be made for this data. I am also creating a choropleth map in R for every pollutant including PM2.5, NO2,  SO2 , and O3. On top of this, I am also creating a regression plot between each pollutant and preventable hospitalizations. This is done through the usage of nycgeo as a package to create boundaries. Nycgeo is used over UHF json boundaries because it provides more accurate coastal boundaries. The other packages I am using are tidyverse and sf to join objects and to plot with ggplot. I am left joining the data to create one variable containing all the data. This is something that is true in both plots, but some areas do not have data like Bronx Park and Pelham Bay Park. I do not know why there is no data, but my guess would be that it is a majorly park dominated area, so there are no hospitals or sensors in the region. It is important to note that R pollutant measurements are made in parts per billion. (ppb)

**Data Citation**

<https://public.tableau.com/views/NewYorkCityNeighborhoodHealthAtlas/Home?:language=en-US&:display_count=n&:origin=viz_share_link> (R Analysis)

<https://nycgeo.mattherman.info> (R GIS)

<https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu> (Python Analysis)

<https://data.cccnewyork.org/data/table/6/asthma-emergency-department-visits#6/9/22/a/a> (Python Analysis)

<https://www1.nyc.gov/site/doh/data/health-tools/maps-gis-data-files-for-download.page> (Python GIS)

**Github Code Link**

<https://github.com/zahmed333/Bronx-Pollution-Asthma-Analysis>

Results
` `![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.001.png)
**Figure 1:** Choropleth map of asthma hospitalizations by neighborhood within the Bronx to be compared with the rest of the maps.

![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.002.png)![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.003.png)

**Figure 2:** Choropleth map of PM2.5 and regression analysis of PM2.5 and preventable asthma hospitalizations![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.004.png)

![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.005.png)

**Figure 3**: Choropleth map of Ozone and regression analysis of Ozone and preventable asthma hospitalizations

**Figure 4:** Choropleth map of Sulfur Dioxide and regression analysis of Sulfur Dioxide and preventable asthma hospitalizations![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.006.png)![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.007.png)![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.007.png)

![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.008.png)**Figure 5**: Choropleth map of Nitrogen Dioxide and regression analysis of Nitrogen Dioxide and preventable asthma hospitalizations

![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.009.png)

**Figure 6:**  Satellite Image of the Bronx to visualize urban landscape and greenery

![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.010.png)

**Figure 7:** Mean pollutant values of pollutants in The Bronx (Made in Python)

![](Aspose.Words.de21e25a-2f29-4c89-a926-5c8296179c87.011.png)

**Figure 8:**  Percentage of pollutants found in The Bronx (Made in Python)

**Analyzing results**

`	`One thing we can note is the dangerous levels of pollutants and visits to the South Bronx area. This area connects to Manhattan and there are a multitude of expressways which have heavy traffic all around. Since NYC is so densely populated, these roads act as a bottleneck for automobiles and store up all types of pollutants. Nitrogen Dioxide and particulate matter have clear positive correlations with the amount of hospitalizations as we can see from figures 2 and 5. However, when we look at figure 3 and 4 we don’t see the same. Figure 3 shows that Ozone has a negative correlation in relation to hospitalizations. To add on, figure 4 of Sulfur Dioxide shows little to no correlation. These two results are trivial and I don’t have an answer for this. My only clue is that it is some sort of error because previous work points against this (Warman et al, 2009) and the high-level areas for figures 3 and 4 are near parks, according to figure 6, which should take away from pollution levels rather than adding to them. Even after double checking my results and datasets, they seem right. Moving on, figure 8 shows that Nitrogen Dioxide makes up approximately half of the pollutants in The Bronx. This is important, because pollutants with a positive correlation in relation to hospitalizations make up ~75% of the pollutants. We can also supplement with figure 8, where we can see that higher pollutants are in southern neighborhoods.
# Discussion
**Answer to my Research Question**

`	`Despite the outlying pollutants, most air pollutants come together to increase asthma hospitalizations and even create a death rate. Evidence suggests that the reason for a death rate is because the only time people get treated for asthma is often in the emergency room. (Warman et al, 2009) Overall, There lies a positive correlation with the amount of hospitalizations and air pollutants within an area.

**My results compared to previous work**

Many other people have attempted to find a connection between air pollution and asthma rates within the Bronx. One such paper examined the air quality near schools and playgrounds to see if they are affected by traffic-induced pollution. This paper specialized in observing effects of air pollution on children. Their result was that heavy traffic does have an impact on the air quality of the playgrounds in which children, which therein affects the health of the children as well. (Gonzalez, 2021)

**Where does all the pollution come from?**

There are obvious roots to all the pollutants referenced within this paper. One common form of pollution is exhaust from automobiles. Research suggests that multiple factors play into this. For instance, the burning of a gas stove to make a house warm which pollutes the air with nitrogen dioxide (NO2). (Warman et al, 2009) Another risk factor is environmental tobacco smoke. In 2020, approximately 14% of Bronx citizens smoke tobacco products according to the NYCSmokeFree organization which is the second highest rate out of the boroughs in New York City. (*Smoking Rates*, 2021) This second-hand smoke alone produces a multitude of toxic pollutants that is a huge risk factor for people to become hospitalized for their asthma. 

**Why does this matter?**
**
`	`This is such an important issue because The Bronx is a low income neighborhood and air pollution creates more obstacles for disadvantaged citizens. Long-period residents worrying about how they can afford livelihood in such an expensive area, will now also have health issues to worry about. After living in The Bronx for 15 years, I have also developed low-level asthma along with my mother, despite having no genetic predisposition. The first time I found out was when I had an asthma attack after joining the track team at my high-school during a track-meet. An important quote that shows why this matters is: “The color of your skin and your economic status should not determine the quality of the air you breathe.” (Bronx Gets Another Boost Toward a Clean Air Future, Johnson, 2022) Another point is that, The money we spend in healthcare would be made back if the money went into improving the quality of life. This point is furthered through the quote, “​​Capping the Cross Bronx Expressway and filtering the air, even though it is quite expensive to do so, would pay for itself by reducing health costs in this region.” (Bronx Gets Another Boost Toward a Clean Air Future, 2022) 

**What has been done about it?**

`	`There have been two main actions that have been done about the issue at-hand. One of them is to bring awareness to the problem. One of the major things that has recently been established is the Environmental Justice Air Monitoring Act. This act helps to “Fund a network of air monitors to understand the health risks of air pollution block by block.” (Bronx Gets Another Boost Toward a Clean Air Future, 2022) This will help establish more data that can be presented in papers and posters to bring awareness. Furthermore, non-profit organizations like South Bronx Unite organize protests across the city to raise awareness. The other main action is to have begun renovations. The biggest renovation so far has been the Sheridan Expressway. Governor Cuomo spent $75 million on the Sheridan Expressway project that gave greenspace back to the Bronx River. This also turned a highway into a pedestrian friendly boulevard. (Bronx Times, 2019).

**What can be done about it?**

`	`One possible solution to the abundance of air pollution is to add a vegetative barrier between public spaces and the roads. This can mean adding a wall of trees blocking the particulate matter from entering public spaces like sidewalks and parks. From our data we concluded that PM2.5 is a clear factor that affects asthma rates in The Bronx. According to Diener’s research on green spaces, they can improve the quality of the air we breathe in. (Diener, 2021) Green spaces are best defined as an exposure to greenery. What I am proposing is for green spaces to occupy more areas of public spaces in The Bronx. One point that I can provide from my personal experience is when I used to live in The Bronx, one of the main things that shocked me when I visited other cities was the amount of greenery. This shock comes at no surprise, as we can see from the satellite image from figure 6, there is one big space of greenery in the middle, and then a park on the East side of the Bronx called Pelham Bay Park. If there were more greenery, it can absorb many of the pollutants like carbon dioxide and particulate matter.

`	`Another solution could be to break up the bottleneck created by the small amount of expressways, that way there wouldn’t be such heavy traffic in just certain areas, and allow it to disperse equally. This would make South Bronx less polluted. However, this comes with its flaws as it won’t really change the amount of pollutants in the area. It is a trade, and probably wouldn’t be worth the amount of money put into making new major roads.


# **
# References
Maantay, Juliana. (2007). Asthma and air pollution in the Bronx: Methodological and data considerations in using GIS for environmental justice and health research. Health & place. 13. 32-56. 10.1016/j.healthplace.2005.09.009

U.S. Census Bureau (2020). Quick Facts Bronx County, New York. https://www.census.gov/quickfacts/fact/table/bronxcountynewyork/PST045221

Spira et al (2011)., “Personal Exposures to Traffic-Related Air Pollution and Acute Respiratory Health among Bronx Schoolchildren with Asthma.”

Juliana A. Maantay, Andrew R. Maroko & Holly Porter-Morgan (2008) Research Note—A New Method for Mapping Population and Understanding the Spatial Dynamics of Disease in Urban Areas: Asthma in the Bronx, New York, Urban Geography, 29:7, 724-738

Gonzalez, J. (2021). AIR POLLUTANTS AND CHILDHOOD ASTHMA IN THE BRONX - Jovan Gonzalez\*, Veronique Lankar, Yelda Hangun-Balkir. Westmont College. Retrieved May 7, 2022, from https://www.westmont.edu/sites/default/files/2021-08/Jovan%20Gonzalez.pdf

Diener, A., &amp; Mudu, P. (2021, June 24). How can vegetation protect us from air pollution? A critical review on Green Spaces' mitigation abilities for air-borne particles from a public health perspective - with implications for urban planning. Science of The Total Environment. Retrieved May 7, 2022, from https://www.sciencedirect.com/science/article/pii/S0048969721036779

Warman, K., Silver, E. J., & Wood, P. R. (2009). Modifiable risk factors for asthma morbidity in Bronx versus other inner-city children. The Journal of asthma : official journal of the Association for the Care of Asthma, 46(10), 995–1000. https://doi.org/10.3109/02770900903350481

SMOKING RATES IN NEW YORK CITY- STATS. (2021, June). NYC Smoke Free. Retrieved May 10, 2022, from https://nycsmokefree.org/resources/smoking-statistics/

Figure 6: The Bronx map // USA, New York. (n.d.). Satellite map. Retrieved May 13, 2022, from <https://satellites.pro/The_Bronx_map#40.846086,-73.879795,13>

Air Pollution and Asthma | AAFA.org. (2015). Asthma and Allergy Foundation of America | AAFA. Retrieved May 12, 2022, from <https://www.aafa.org/air-pollution-smog-asthma/>

Davidson, A. (2012, July 10). Why Can't the Bronx Be More Like Brooklyn? (Published 2012). The New York Times. Retrieved May 6, 2022, from https://www.nytimes.com/2012/07/15/magazine/bronx-economy.html

Bronx Gets Another Boost Toward a Clean Air Future | Columbia Public Health. (2022, April 25). Columbia University's Mailman School of Public Health. Retrieved May 12, 2022, from https://www.publichealth.columbia.edu/public-health-now/news/bronx-gets-another-boost-toward-clean-air-future

Sheridan Expressway's removal project is completed – Bronx Times. (2019, December 20). Bronx Times. https://www.bxtimes.com/sheridan-expressways-removal-project-is-completed/

https://satellites.pro/The\_Bronx\_map#40.846086,-73.879795,13

Warman, K., Silver, E. J., & Wood, P. R. (2009). Modifiable risk factors for asthma morbidity in Bronx versus other inner-city children. The Journal of asthma : official journal of the Association for the Care of Asthma, 46(10), 995–1000.

Takizawa H. (2015). Impacts of Particulate Air Pollution on Asthma: Current Understanding and Future Perspectives. Recent patents on inflammation & allergy drug discovery, 9(2), 128–135. <https://doi.org/10.2174/1872213x09666150623110714>

*The Particulars of PM 2.5*. (2014, November 14). NRDC. Retrieved May 13, 2022, from <https://www.nrdc.org/onearth/particulars-pm-25>

*Sulfur Dioxide* (2020). American Lung Association. Retrieved May 13, 2022, from https://www.lung.org/clean-air/outdoors/what-makes-air-unhealthy/sulfur-dioxide

