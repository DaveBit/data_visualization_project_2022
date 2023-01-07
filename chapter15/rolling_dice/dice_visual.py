from die import Die
import pygal


# Create two dice D6
die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list.
results = [die_1.roll() + die_2.roll() for roll_number in range(1000)]
"""
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
"""

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in (2, max_result+1)]
"""
for value in range(Die.instance_counter.total(), (max_result+1)):  # range() does not include the last number.
    frequency = results.count(value)
    frequencies.append(frequency)
"""

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(Die.instance_counter.total(), (Die.instance_counter.total()*6)+1)]
# [str(x) for x in range(2, 13)]
# Better not to use this solution since is useful just for two dice.
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
"""
The add method is called to add a series of data to the bar chart.
The first argument is the name of the series 
and the second argument is a list of values."""

hist.render_to_file('dice_visual6-6.svg')
