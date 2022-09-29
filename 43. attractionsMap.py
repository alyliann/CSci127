#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 2, 2021
#This program asks for a CSV file and maps all the NYC attractions on that file

import folium
import pandas as pd

inF = input("Enter CSV file name: ") #attractions.csv
outF = input("Enter output file: ") #thMap.html

attractions = pd.read_csv(inF)
print(attractions['NAME'])

attMap = folium.Map(
    location=[0, 0],
    tiles='Cartodb Positron'
)

for index,row in attractions.iterrows():
    lat = row['LATITUDE']
    lon = row['LONGITUDE']
    name = row['NAME']
    newMarker = folium.Marker(location=[lon, lat], popup=name)
    newMarker.add_to(attMap)

attMap.save(outfile=outF)
