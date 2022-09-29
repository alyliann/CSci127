#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 26, 2021
#This program reads a CSV of video game data

import pandas as pd

inF = input("Enter file name: ")    #vgsales.csv
vgsales = pd.read_csv(inF)

tot = int(vgsales['Rank'].max()) #OR: vgsales['Rank'].value_counts()[-1:] #???
print("There are", (tot - 2), "total games")

print("The number of games in each genre is")
genres = vgsales['Genre'].value_counts()
print(genres)

print("The top 3 game publishers are")
top3 = vgsales['Publisher'].value_counts()[:3]
print(top3)
