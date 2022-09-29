#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 2, 2021
#This program creates a map centered at Little Island in Chelsea Piers

import folium

#Create map centered at Little Island
myMap = folium.Map(
    location=[40.75, -74.125],
    zoom_start=3
)

#Make Little Island marker
mark = folium.Marker(location=[40.7420577, -74.0101494], popup='Little Island')

#Add that Little Island marker to the map
mark.add_to(myMap)

#Save the map as HTML file
myMap.save(outfile="nycMap.html")
