from random import randint
from collections import Counter


class Die:
    """A class representing a single die."""
    instance_counter = Counter()  # class attribute to track the number of instances

    def __init__(self, num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides
        Die.instance_counter[self] += 1  # class attribute to track the number of instances

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
        #  randint returns a number between 1 and 6 (both included)
