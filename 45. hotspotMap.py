#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 2, 2021
#This program creates a map of HotSpots in NYC

import folium
import pandas as pd

inF = input("Please enter the name of the input file: ") #NYC_Wi-Fi_Hotspot_Locations.csv
outF = input("Please enter the name of the output file: ") #manhattan.html
borough = input("Please enter the name of the borough: ") #Manhattan

hotspots = pd.read_csv(inF)
grouped = hotspots.groupby('City').get_group(borough)

hotMap = folium.Map(location=[0, 0])

for index,row in grouped.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    name = row['Location']
    newMarker = folium.Marker(location=[lat, lon], popup=name)
    newMarker.add_to(hotMap)

hotMap.save(outfile=outF)
