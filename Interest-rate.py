import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('Interestrate.csv')

# Extract the data for the x-axis and y-axis
x = data['Observation Date']
y = data['Observation Value']

x=x[::4]
y=y[::4]
plt.figure(figsize=(10, 4))
plt.gca().invert_xaxis()
plt.xlabel("Monetary Policy Dates")
plt.ylabel("Interest Rate")

plt.step(x,y)
plt.title("Interest Rates")
plt.show()
