import matplotlib.pyplot as plt

# National inflation rate
x = [10.7, 9.2, 11.5, 12.3, 13, 12.2, 12.7, 13.8, 13.8, 21.3, 24.9]
# Urban inflation rate
z = [10.2, 9.6, 12, 12.7, 13, 11.5, 11.9, 12.2, 12.4, 19.8, 23.6]
# Interest rate
y = [10, 9.75, 9.75, 9.75, 10.75, 13.25, 11, 13.25, 13.25, 14.75, 14.75]

# Create scatter plot
plt.scatter(x, y, label='National Inflation')
plt.scatter(z, y, label='Urban Inflation')

# Add legend
plt.legend()

# Add axis labels and title
plt.xlabel('Inflation Rate')
plt.ylabel('Interest Rate')
plt.title('Scatter Plot: Inflation Rate vs. Interest Rate')

# Set x-axis and y-axis limits
plt.xlim(9, 14)
plt.ylim(9, 14)

# Add time indicator
plt.axvline(x=9.1, color='red', linestyle='--', label='Time Indicator')
plt.axvline(x=13.8, color='red', linestyle='--')

# Add time labels
plt.annotate('2020', xy=(9.1, 9.5), xytext=(9.1, 9.7), color='red', ha='center')
plt.annotate('2022', xy=(13.8, 9.5), xytext=(13.8, 9.7), color='red', ha='center')

# Display the plot
plt.show()
