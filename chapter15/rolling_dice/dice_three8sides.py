import pygal
from die import Die

# Creating 3 6sided dice.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Rolling it a determinate number of times.
results = [die_1.roll() + die_2.roll() + die_3.roll() for x in range(1000000)]

# Analyzing the results.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(x) for x in range(3, max_result+1)]

# Using pygal to show the results.

hist2_8 = pygal.Bar()

hist2_8.title = "Results of rolling two D8 dice 10,000,000 times."

hist2_8.add("D6+D6+D6", frequencies)
hist2_8.x_labels = [str(x) for x in range(3, max_result+1)]
hist2_8.x_title = "Number of sides"
hist2_8.y_title = "Frequency of result"
hist2_8.render_to_file("dice_visual_three6sides.svg")