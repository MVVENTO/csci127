import matplotlib.pyplot as plt
import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
print(pop)
pop["frac"] = pop['Manhattan']/pop['Total']
print(pop)
pop.plot(x="Year", y ="frac")
plt.show()
