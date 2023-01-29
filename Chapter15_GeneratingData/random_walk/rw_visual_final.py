import matplotlib.pyplot as plt
from random_walk_final import RandomWalk

while True:

    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(12, 6))

    point_numbers = list(range(rw.num_points))  # Refresher, range is a function that returns a sequence of numbers.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=10)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove the axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.savefig('rw_visual_final.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

