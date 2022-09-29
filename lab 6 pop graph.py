import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
pop.plot(x="Year")

plt.show()

print("The largest number living in the Bronx is", pop["Bronx"].max())
