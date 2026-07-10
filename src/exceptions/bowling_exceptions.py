"""i created custom exceptions for the bowling game"""


class BowlingGameError(Exception):
    """Base exception"""
    pass


class ValidationError(BowlingGameError):
    """Base validation exception"""
    pass


class InvalidGameError(ValidationError):
    """raised when the game is invalid"""
    pass


class InvalidFrameCountError(InvalidGameError):
    """raised when frame count is not 10"""
    pass


class InvalidFrameError(ValidationError):
    """raised when a frame is invalid"""
    pass


class InvalidRollError(ValidationError):
    """raised when a roll is invalid"""
    pass


class InvalidSymbolError(InvalidRollError):
    """raised for invalid bowling symbols"""
    pass