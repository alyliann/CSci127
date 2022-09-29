#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 19, 2021
#This program creates a graph of UFO sighting times by state

import matplotlib.pyplot as plt
import pandas as pd

inF = input("Enter name of input file: ")
outF = input("Enter name of output file:  ")

df = pd.read_csv(inF)
groupedData = df.groupby('state')['duration (seconds)'].mean().sort_values(ascending=False)[:10]
groupedData.plot.bar()

plt.xlabel('State')
plt.ylabel('Seconds')


fig = plt.gcf()
fig.savefig(outF)
