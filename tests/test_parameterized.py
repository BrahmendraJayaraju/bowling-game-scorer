"""parameterized scoring tests"""

import allure
import pytest

from src.engine.parser import GameParser
from src.engine.scorer import BowlingScorer

from src.exceptions.bowling_exceptions import (
    InvalidFrameCountError,
    InvalidFrameError,
InvalidRollError,
    InvalidSymbolError,
)

from testdata.valid_games import *
from testdata.invalid_games import *


@allure.feature("Bowling Game with parameterization")
@allure.story("parameterized all valid and invalid scenarios")
@allure.title("verify bowling game scoring and validation with parameterization ")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "game, expected_score, expected_exception",
    [

        # for valid scenario

        (EXAMPLE_GAME, EXAMPLE_GAME_SCORE, None),
        (PERFECT_GAME, PERFECT_GAME_SCORE, None),
        (ALL_SPARES, ALL_SPARES_SCORE, None),
        (ALL_OPEN, ALL_OPEN_SCORE, None),
        (TENTH_FRAME_STRIKE, TENTH_FRAME_STRIKE_SCORE, None),
        (TENTH_FRAME_SPARE, TENTH_FRAME_SPARE_SCORE, None),
        (TENTH_FRAME_OPEN, TENTH_FRAME_OPEN_SCORE, None),
        (GUTTER_GAME, GUTTER_GAME_SCORE, None),

        # for invalid scenario

        (SPARE_FIRST_ROLL, None, InvalidRollError),
        (INVALID_SYMBOL, None, InvalidSymbolError),
        (FRAME_EXCEEDS_TEN, None, InvalidFrameError),
        (INVALID_STRIKE_SECOND_ROLL, None, InvalidRollError),
        (TOO_MANY_ROLLS_TENTH_FRAME, None, InvalidFrameError),
        (FOUR_ROLLS_TENTH_FRAME, None, InvalidFrameError),
        (LESS_THAN_TEN_FRAMES, None, InvalidFrameCountError),
        (MORE_THAN_TEN_FRAMES, None, InvalidFrameCountError),
        (EXTRA_FRAME_AFTER_GAME, None, InvalidFrameCountError),

    ],
    ids=[
        "Example Game",
        "Perfect Game",
        "All Spares",
        "All Open",
        "Tenth Frame Strike",
        "Tenth Frame Spare",
        "Tenth Frame Open",
        "Gutter Game",

        "Spare First Roll",
        "Invalid Symbol",
        "Frame Exceeds Ten",
        "Strike Second Roll",
        "Too Many Rolls Tenth",
        "Four Rolls Tenth",
        "Less Than Ten Frames",
        "More Than Ten Frames",
        "Extra Frame After Game",
    ],
)
def test_bowling_game_scenarios(
    game,
    expected_score,
    expected_exception,
):

    scorer = BowlingScorer()

    parsed_game = GameParser.parse(game)

    if expected_exception is not None:

        with pytest.raises(expected_exception):
            scorer.score(parsed_game)

    else:

        actual_score = scorer.score(parsed_game)

        if isinstance(expected_score, list):
            assert actual_score == expected_score
        else:
            assert actual_score[-1] == expected_score