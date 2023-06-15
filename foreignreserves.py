import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('ForeignReserves.csv')

# Extract the data for the x-axis and y-axis
x = data['Observation Date']
y = data['Observation Value']

# Extract every 30th value starting from the second row
x = x[1::60]
y = y[1::60]
#x=x[-4:]
#y=y[-4:]
plt.plot(x, y)

plt.xlabel('Years')
plt.ylabel('Reserves In Million USD')
plt.title('Foreign Reserves')

# Reverse the x-axis and y-axis
plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()

# Annotate the data points with their values
for i, j in zip(x, y):
    plt.annotate(str(j), xy=(i, j), xytext=(-10, 10), textcoords='offset points')

# Display the graph
plt.show()
