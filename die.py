from random import randint, choices

class Die:
    """ A class representing a single die object."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        self.outcomes = range(1, num_sides+1)

    def set_fair_die_dist(self):
        uniform_prob = 1/self.num_sides
        prob_dict = {}
        for i in self.outcomes:
            prob_dict[i] = uniform_prob
        self.fair_die_dist =  prob_dict

    def roll_once(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    def roll_n(self, n):
        """Roll Die n times"""
        return choices(self.outcomes, k=n)


