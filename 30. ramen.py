#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 12, 2021
#This program prints the lowest rating for a ramen spot in Singapore

import matplotlib.pyplot as plt
import pandas as pd

file = input("Enter file name:")
ramen = pd.read_csv(file)

print("The average stars per serving style:")

style = ramen.groupby('Style')
print(style['Stars'].mean())

stars = ramen.groupby('Stars')

singapore = ramen.groupby('Country').get_group('Singapore')
singaporeMin = singapore['Stars'].min()

print("KOKA has the lowest rating in Singapore with", singaporeMin, "stars.")
