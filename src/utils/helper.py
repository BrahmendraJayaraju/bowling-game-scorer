"""common helper functions for the boowling game scorer"""

from src.engine.constants import STRIKE, SPARE


class Helper:
    """utility methods"""

    @staticmethod
    def is_strike(symbol):
        """returns True if the symbol is a strike"""
        return symbol.upper() == STRIKE

    @staticmethod
    def is_spare(symbol):
        """returns True if the symbol is a spare"""
        return symbol == SPARE

    @staticmethod
    def pin_value(symbol, previous=0):
        """this will convert a roll symbol into pin count """

        if Helper.is_strike(symbol):
            return 10

        if Helper.is_spare(symbol):
            return 10 - previous

        return int(symbol)