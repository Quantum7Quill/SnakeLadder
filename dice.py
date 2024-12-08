import random
class Dice:
    def __init__(self, minimum_value = 1, maximum_value = 6):
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        
    def roll(self):
        return random.randint(self.minimum_value, self.maximum_value)