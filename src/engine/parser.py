"""parses raw bowling input into a game object"""

from src.models.game import Game


class GameParser:
    """parses bowling input"""

    @staticmethod
    def parse(frames):

        return Game(frames)