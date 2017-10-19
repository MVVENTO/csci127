import pandas as pd
import matplotlib.pyplot as plt

homeless = pd.read_csv("DHS_Daily_Report.csv")
homeless.plot(x = "Date of Census")
plt.show()


