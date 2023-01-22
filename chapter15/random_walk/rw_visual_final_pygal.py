import pygal
from random_walk_final import RandomWalk

while True:

    # Make a random walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Create a line chart
    line_chart = pygal.Line()

    # Add the x and y values to the chart
    line_chart.add('Random Walk', list(zip(sorted(rw.x_values),sorted(rw.y_values))))

    # Emphasize the first and last points
    line_chart.add('Start', [0, 0])
    line_chart.add('End', [rw.x_values[-1], rw.y_values[-1]])

    # Remove the x and y axis
    line_chart.x_label = None
    line_chart.y_label = None

    # Render the chart
    line_chart.render_to_file('random_walk.svg')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
