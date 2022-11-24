from random import randint 

class Die:
    """ A class representing a single die object."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def fair_die_dist(self):
        uniform_prob = 1/self.num_sides
        prob_dict = {}
        for i in range(1, self.num_sides+1):
            prob_dict[i] = uniform_prob
        return prob_dict

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)