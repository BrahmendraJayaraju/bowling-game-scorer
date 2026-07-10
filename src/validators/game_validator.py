"""validates a bowling game"""

from src.engine.constants import (
    TOTAL_FRAMES,
    MAX_PINS,
    VALID_SYMBOLS,
)

from src.exceptions.bowling_exceptions import (
    InvalidFrameCountError,
    InvalidFrameError,
    InvalidSymbolError,
InvalidRollError,
)

from src.utils.helper import Helper


class GameValidator:

    @staticmethod
    def validate(game):
        GameValidator._validate_frame_count(game)

        for index, frame in enumerate(game):

            GameValidator._validate_symbols(frame)

            if index < 9:
                GameValidator._validate_regular_frame(frame)
            else:
                GameValidator._validate_tenth_frame(frame)

    @staticmethod
    def _validate_frame_count(game):

        if len(game) != TOTAL_FRAMES:
            raise InvalidFrameCountError(
                f"game must contain exactly {TOTAL_FRAMES} frames"
            )

    @staticmethod
    def _validate_symbols(frame):

        for roll in frame:

            if roll.symbol not in VALID_SYMBOLS:
                raise InvalidSymbolError(
                    f"invalid symbol: {roll.symbol}"
                )

    @staticmethod
    def _validate_regular_frame(frame):

        # strike
        if len(frame) == 1:

            if not Helper.is_strike(frame[0].symbol):
                raise InvalidFrameError(
                    "single roll frame must be a strike"
                )

            return

        if len(frame) != 2:
            raise InvalidFrameError(
                "regular frame must contain one or 2 rolls"
            )

        first = frame[0].symbol
        second = frame[1].symbol

        if Helper.is_spare(first):
            raise InvalidRollError(
                "spare cannot be 1st roll"
            )

        if Helper.is_strike(second):
            raise InvalidRollError(
                "strike cannot be second roll"
            )

        if Helper.is_spare(second):
            return

        total = int(first) + int(second)

        if total > MAX_PINS:
            raise InvalidFrameError(
                "frame pin count exceeds 10"
            )

    @staticmethod
    def _validate_tenth_frame(frame):

        if len(frame) < 2 or len(frame) > 3:
            raise InvalidFrameError(
                "invalid tenth frame"
            )

        first = frame[0].symbol
        second = frame[1].symbol

        if Helper.is_spare(first):
            raise InvalidFrameError(
                "spare cannot be first roll"
            )

        # strike   may have 3 rolls
        if Helper.is_strike(first):
            return

        # spare must have bonus roll
        if Helper.is_spare(second):

            if len(frame) != 3:
                raise InvalidFrameError(
                    "spare in tenth requires one bonus roll"
                )

            return

        # open frame

        total = int(first) + int(second)

        if total > MAX_PINS:
            raise InvalidFrameError(
                "frame pin count exceeds 10"
            )

        if len(frame) != 2:
            raise InvalidFrameError(
                "open 10 frame cannot have bonus roll"
            )