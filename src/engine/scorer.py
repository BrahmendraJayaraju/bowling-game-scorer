"""contains the bowling scoring logic"""

from src.validators.game_validator import GameValidator


class BowlingScorer:
    """this will Calculates the cumulative score of a bowling game"""

    def score(self, game):
        """returns cumulative score after each frame"""
        GameValidator.validate(game)

        cumulative_scores = []
        running_total = 0

        for index in range(len(game)):
            frame_score = self._frame_score(game, index)

            running_total = running_total+frame_score

            cumulative_scores.append(running_total)

        return cumulative_scores

    def _frame_score(self, game, index):

        frame = game[index]

        # 10th frame
        if index == 9:
            return self._tenth_frame_score(frame)

        # strike
        if self._is_strike(frame):
            return 10 + self._strike_bonus(game, index)

        # spare
        if self._is_spare(frame):
            return 10 + self._spare_bonus(game, index)

        # open frame
        return self._open_frame_score(frame)

    def _is_strike(self, frame):
        return (
                len(frame) == 1
                and frame[0].symbol.upper() == "X"
        )

    def _is_spare(self, frame):
        return (
                len(frame) >= 2
                and frame[1].symbol == "/"
        )

    def _open_frame_score(self, frame):

        total = 0

        previous = 0

        for roll in frame:
            value = self._roll_value(
                roll.symbol,
                previous
            )

            total += value

            previous = value

        return total

    def _roll_value(self, symbol, previous=0):

        if symbol.upper() == "X":
            return 10

        if symbol == "/":
            return 10 - previous

        return int(symbol)

    def _tenth_frame_score(self, frame):

        total = 0
        previous = 0

        for roll in frame:
            value = self._roll_value(
                roll.symbol,
                previous
            )

            total += value
            previous = value

        return total

    def _spare_bonus(self, game, index):

        next_frame = game[index + 1]

        return self._roll_value(
            next_frame[0].symbol
        )

    def _strike_bonus(self, game, index):

        values = []

        for frame in game[index + 1:]:

            previous = 0

            for roll in frame:

                value = self._roll_value(
                    roll.symbol,
                    previous
                )

                values.append(value)

                previous = value

                if len(values) == 2:
                    return sum(values)

        return sum(values)



