"""tells a single roll in a bowling game"""


class Roll:


    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol