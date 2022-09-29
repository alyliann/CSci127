import pandas as pd

rain = pd.read_csv('AustraliaRain.csv')

groupedData = rain.groupby('Location')
print(groupedData['Rainfall'].mean())

#or:

print(rain.groupby('Location')['Rainfall'].mean())

#for one location:

albury = rain.groupby('Location').get_group('Albury')
print(albury['Rainfall'].mean())
