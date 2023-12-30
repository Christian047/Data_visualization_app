# Import relevant library
import matplotlib.pyplot as plt  # Correct import statement

# Assign values to x and y axis
x1 = [2, 3, 4, 4]
y1 = [5, 6, 7, 11]

# Plot the first graph
plt.plot(x1, y1, label='Line 1')

x2 = [1, 3, 6, 12]
y2 = [2, 6, 8, 10]

# Plot the second graph
plt.plot(x2, y2, label='Line 2')

# Name the x and y axis
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Name the Graph title
plt.title('Demo Graph - Two lines')

# Add a legend for better readability
plt.legend()

# Show the graph
plt.show()

print('Done')
