import pygal
from random_walk_final import RandomWalk

# Making two instances of a random class walk.
rw = RandomWalk(5000)
rw.fill_walk()

# Making the XY chart with pigal.
xy_chart = pygal.XY(stroke=False)
xy_chart.title = "Random Walk"

# Utilizing zip to make a list of tuples [(0,1), (2,9)...]
xy_chart.add("", list(zip(rw.x_values, rw.y_values)))

# Rendering png and svg files of the exercise.
xy_chart.render_to_file("rw_visual_final_pygal.svg")
xy_chart.render_to_file("rw_visual_final_pygal.png")
