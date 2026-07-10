
"""represents a complete bowling game"""

from src.models.frame import Frame


class Game:

    def __init__(self, frames):
        self.frames = [Frame(frame) for frame in frames]

    def __iter__(self):
        return iter(self.frames)

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, index):
        return self.frames[index]

    def __repr__(self):
        return str(self.frames)