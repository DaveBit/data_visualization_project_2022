import matplotlib.pyplot as plt
from die import Die

# Create a D6
die = Die()

# Make some rolls and store the results in a list.
results = [die.roll() for roll_num in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results.
plt.bar(range(1, die.num_sides+1), frequencies)
plt.title("Results of rolling one D6 1000 times.")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.savefig("die_visual_matplotlib.png")
plt.show()

