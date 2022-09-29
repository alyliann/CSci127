#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 19, 2021
#This program creates a graph of % of winning SuperBowl points vs time

import matplotlib.pyplot as plt
import pandas as pd

inF = input("Enter name of input file:  ") #Superbowl_Finals.csv
outF = input("Enter name of output file:  ") #results.png

df = pd.read_csv(inF)
df['Date'] = pd.to_datetime(df['Date'].apply(str))
df['% Points'] = 100 * df["Winner Pts"] / (df["Winner Pts"] + df["Loser Pts"])
df.plot(x='Date', y='% Points')

fig = plt.gcf()
fig.savefig(outF)
