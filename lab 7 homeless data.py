import matplotlib.pyplot as plt
import pandas as pd

homeless = pd.read_csv("DHS_Daily_Report.csv")
homeless.plot(x="Date of Census", y="Total Individuals in Shelter")
plt.show()
