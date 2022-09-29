import folium
import pandas as pd

cuny = pd.read_csv('CUNYcampuses.csv')
print(cuny["Campus"])

mapCUNY = folium.Map(location=[40.768731, -73.964915])

for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

mapCUNY.save(outfile='cunyLocations.html')
