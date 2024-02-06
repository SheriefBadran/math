import matplotlib.pyplot as plot

# Create a figure
figure = plot.figure()

# Add axes to the figure
axis = figure.add_subplot(1, 1, 1)

# Plot data on the axes
axis.plot([1, 2, 3], [4, 5, 6])

# Show the plot
plot.show()