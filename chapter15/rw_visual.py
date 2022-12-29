import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))  # Refresher, range is a function that returns a sequence of numbers.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

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
