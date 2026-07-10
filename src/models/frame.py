"""represents one frame in a bowling game."""

from src.models.roll import Roll


class Frame:


    def __init__(self, rolls):
        self.rolls = [Roll(symbol) for symbol in rolls]

    def __iter__(self):
        return iter(self.rolls)

    def __len__(self):
        return len(self.rolls)

    def __getitem__(self, index):
        return self.rolls[index]

    def __repr__(self):
        return str([roll.symbol for roll in self.rolls])