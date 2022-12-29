import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break