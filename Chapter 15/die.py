from random import randint


class Die:
    """A main class to generate die"""
    def __init__(self, num_die=6):
        self.num_die = num_die

    def fill(self):
        """A function to make rendom die numbers"""
        return randint(1, self.num_die)