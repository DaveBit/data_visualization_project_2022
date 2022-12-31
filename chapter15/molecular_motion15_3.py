import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(12, 6))

    point_numbers = list(range(rw.num_points))  # Refresher, range is a function that returns a sequence of numbers.
    plt.plot(rw.x_values, rw.y_values, linewidth='1')

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove the axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break