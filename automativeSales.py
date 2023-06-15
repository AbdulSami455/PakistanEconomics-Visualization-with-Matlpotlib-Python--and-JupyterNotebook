import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('automatives-Sales.csv')

# Extract the data for the x-axis and y-axis
x = data['Observation Date']
y = data['Observation Value']

x=x[::60]
y=y[::60]
plt.figure(figsize=(10, 4))
plt.gca().invert_xaxis()
plt.ylabel("Production Units")
#plt.xlabel("Dates")
plt.hist(x)
plt.title("")
plt.show()
