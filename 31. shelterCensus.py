#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 19, 2021
#This program creates a graph of single adults in NYC shelters

import matplotlib.pyplot as plt
import pandas as pd

inF = input("Enter name of input file: ")
outF = input("Enter name of output file: ")

csv = pd.read_csv(inF)
csv['Fraction Single Adults'] = csv['Total Single Adults in Shelter']/csv['Total Individuals in Shelter']
csv.plot(x="Date of Census", y='Fraction Single Adults')

fig = plt.gcf()
fig.savefig(outF)
