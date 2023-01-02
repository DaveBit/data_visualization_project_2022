from die import Die
import pygal


# Create a D6
die = Die()

# Make some rolls and store the results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):  # range() does not include the last number.
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
"""
The add method is called to add a series of data to the bar chart.
The first argument is the name of the series 
and the second argument is a list of values."""
hist.render_to_file('die_visual.svg')
