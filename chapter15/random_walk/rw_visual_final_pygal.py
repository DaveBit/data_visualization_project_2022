import pygal
from random_walk_final import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

xy_chart = pygal.XY(stroke=False)
xy_chart.title = "Random Walk"

xy_chart.add("", list(zip(rw.x_values, rw.y_values)))

xy_chart.render_to_file("rw_visual_final_pygal.svg")
xy_chart.render_to_file("rw_visual_final_pygal.png")
