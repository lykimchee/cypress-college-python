import random


class Dice:
    def __init__(self):
        self.cur_side = 1

    def roll(self):
        self.cur_side = random.randint(1, 6)
