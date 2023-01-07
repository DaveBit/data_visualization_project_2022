from die import Die
import pygal

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)


# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(Die.instance_counter.total(), max_result+1):  # range() does not include the last number.
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times"
hist.x_labels = hist.x_labels = \
    [str(x) for x in range(Die.instance_counter.total(), (die_1.num_sides+die_2.num_sides)+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Results"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual10-6.svg')

