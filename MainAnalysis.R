library(nycgeo)
#NYCGEO is the best spatial mapping of nyc available
library(sf)
library(tidyverse)

#Will differ depending on the system, file is available on the repo
nta_health <- read_csv("~/Desktop/nta-health.csv") %>% 
  select(NTA_Code, PM25, Ozone, SulfurDioxide, NitrogenDioxide, PreventHospAsthma)

#Subsetting all the rows to Bronx
nta_health = nta_health[52:89, ]

#Asthma rates to compare
nyc_boundaries(geography = "nta",
               filter_by = "borough",
               region = "bronx",
               add_acs_data = TRUE) %>% 
  left_join(nta_health, by = c("nta_id" = "NTA_Code")) %>% 
  ggplot() +
  geom_sf(aes(fill = PreventHospAsthma)) +
  scale_fill_viridis_c(name = "Hospitalizations", option = "inferno") +
  theme_void() +
  theme(panel.grid = element_line(color = "transparent"), plot.title = element_text(hjust = 0.5)) +
  labs(title = "Preventable Asthma Hospitalizations by Neighborhoods")

nyc_boundaries(geography = "nta",
               filter_by = "borough",
               region = "bronx",
               add_acs_data = TRUE) %>% 
  left_join(nta_health, by = c("nta_id" = "NTA_Code")) %>% 
  ggplot() +
  geom_sf(aes(fill = PreventHospAsthma)) +
  scale_fill_viridis_c(name = "Hospitalizations", option = "inferno") +
  theme_void() +
  theme(panel.grid = element_line(color = "transparent"), plot.title = element_text(hjust = 0.5)) +
  labs(title = "Preventable Asthma Hospitalizations by Neighborhoods")

#Choropleth map
nyc_boundaries(geography = "nta",
               filter_by = "borough",
               region = "bronx",
               add_acs_data = TRUE) %>% 
  left_join(nta_health, by = c("nta_id" = "NTA_Code")) %>% 
  ggplot() +
  geom_sf(aes(fill = PM25)) +
  scale_fill_viridis_c(name = expression(PM^2.5~(Fine ~ Particulate ~ Matter)), option = "inferno") +
  theme_void() +
  theme(panel.grid = element_line(color = "transparent"), plot.title = element_text(hjust = 0.5)) +
  labs(title = "Levels of PM2.5 by Neighborhoods")

#Regression analysis
nta_graph <- ggplot(nta_health, aes(x=PreventHospAsthma, y=PM25))+
  geom_point()+
  geom_smooth(method="lm", col="black")+
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))+
  labs(title = expression(Bronx ~ PM^2.5 ~ Regression ~ Analysis),
       x = "Preventable Asthma Hospitalizations",
       y = expression(PM^2.5~(Fine ~ Particulate ~ Matter) ~ Levels))
nta_graph



nyc_boundaries(geography = "nta",
               filter_by = "borough",
               region = "bronx",
               add_acs_data = TRUE) %>% 
  left_join(nta_health, by = c("nta_id" = "NTA_Code")) %>% 
  ggplot() +
  geom_sf(aes(fill = Ozone)) +
  scale_fill_viridis_c(name = expression(O^3), option = "inferno") +
  theme_void() +
  theme(panel.grid = element_line(color = "transparent"), plot.title = element_text(hjust = 0.5)) +
  labs(title = "Levels of Ozone by Neighborhoods")

nta_graph <- ggplot(nta_health, aes(x=PreventHospAsthma, y=Ozone))+
  geom_point()+
  geom_smooth(method="lm", col="black")+
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))+
  labs(title = expression(Bronx ~ O^3 ~ Regression ~ Analysis),
       x = "Preventable Asthma Hospitalizations",
       y = expression(O^3~(Ozone) ~ Levels))
nta_graph


nyc_boundaries(geography = "nta",
               filter_by = "borough",
               region = "bronx",
               add_acs_data = TRUE) %>% 
  left_join(nta_health, by = c("nta_id" = "NTA_Code")) %>% 
  ggplot() +
  geom_sf(aes(fill = SulfurDioxide)) +
  scale_fill_viridis_c(name = expression(SO^2), option = "inferno") +
  theme_void() +
  theme(panel.grid = element_line(color = "transparent"), plot.title = element_text(hjust = 0.5)) +
  labs(title = "Levels of Sulfur Dioxide by Neighborhoods")

nta_graph <- ggplot(nta_health, aes(x=PreventHospAsthma, y=SulfurDioxide))+
  geom_point()+
  geom_smooth(method="lm", col="black")+
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))+
  labs(title = expression(Bronx ~ SO^2 ~ Regression ~ Analysis),
       x = "Preventable Asthma Hospitalizations",
       y = expression(SO^2~(Sulfur ~ Dioxide) ~ Levels))
nta_graph

nyc_boundaries(geography = "nta",
               filter_by = "borough",
               region = "bronx",
               add_acs_data = TRUE) %>% 
  left_join(nta_health, by = c("nta_id" = "NTA_Code")) %>% 
  ggplot() +
  geom_sf(aes(fill = NitrogenDioxide)) +
  scale_fill_viridis_c(name = expression(NO^2), option = "inferno") +
  theme_void() +
  theme(panel.grid = element_line(color = "transparent"), plot.title = element_text(hjust = 0.5)) +
  labs(title = "Levels of Nitrogen Dioxide by Neighborhoods")

nta_graph <- ggplot(nta_health, aes(x=PreventHospAsthma, y=NitrogenDioxide))+
  geom_point()+
  geom_smooth(method="lm", col="black")+
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))+
  labs(title = expression(Bronx ~ NO^2 ~ Regression ~ Analysis),
       x = "Preventable Asthma Hospitalizations",
       y = expression(NO^2~(Nitrogen ~ Dioxide) ~ Levels))
nta_graph
summary(nta_health)
