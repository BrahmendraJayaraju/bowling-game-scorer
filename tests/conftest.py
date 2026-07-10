""" pytest fixtures"""

import pytest

from src.engine.parser import GameParser

from testdata.valid_games import (
    EXAMPLE_GAME,
    PERFECT_GAME,
    ALL_SPARES,
    ALL_OPEN,
    TENTH_FRAME_STRIKE,
    TENTH_FRAME_SPARE,
    TENTH_FRAME_OPEN,
    GUTTER_GAME,
)

from testdata.invalid_games import (
    SPARE_FIRST_ROLL,
    INVALID_SYMBOL,
    TOO_MANY_ROLLS_TENTH_FRAME,
    FRAME_EXCEEDS_TEN,
    EXTRA_FRAME_AFTER_GAME,

    LESS_THAN_TEN_FRAMES,
    MORE_THAN_TEN_FRAMES,
INVALID_STRIKE_SECOND_ROLL,
FOUR_ROLLS_TENTH_FRAME,

)


@pytest.fixture
def example_game():
    return GameParser.parse(EXAMPLE_GAME)


@pytest.fixture
def perfect_game():
    return GameParser.parse(PERFECT_GAME)


@pytest.fixture
def all_spares():
    return GameParser.parse(ALL_SPARES)


@pytest.fixture
def all_open():
    return GameParser.parse(ALL_OPEN)


@pytest.fixture
def tenth_frame_strike():
    return GameParser.parse(TENTH_FRAME_STRIKE)


@pytest.fixture
def tenth_frame_spare():
    return GameParser.parse(TENTH_FRAME_SPARE)


@pytest.fixture
def tenth_frame_open():
    return GameParser.parse(TENTH_FRAME_OPEN)

@pytest.fixture
def gutter_game():
    return GameParser.parse(GUTTER_GAME)

#invalid TC starts from here

@pytest.fixture
def spare_first_roll():
    return GameParser.parse(SPARE_FIRST_ROLL)


@pytest.fixture
def invalid_symbol():
    return GameParser.parse(INVALID_SYMBOL)

@pytest.fixture
def too_many_rolls_tenth_frame():
    return GameParser.parse(TOO_MANY_ROLLS_TENTH_FRAME)

@pytest.fixture
def frame_exceeds_ten():
    return GameParser.parse(FRAME_EXCEEDS_TEN)



@pytest.fixture
def extra_roll_after_game():
    return GameParser.parse(EXTRA_FRAME_AFTER_GAME)


@pytest.fixture
def less_than_ten_frames():
    return GameParser.parse(LESS_THAN_TEN_FRAMES)


@pytest.fixture
def more_than_ten_frames():
    return GameParser.parse(MORE_THAN_TEN_FRAMES)


@pytest.fixture
def invalid_strike_second_roll():
    return GameParser.parse(INVALID_STRIKE_SECOND_ROLL)


@pytest.fixture
def four_rolls_tenth_frame():
    return GameParser.parse(FOUR_ROLLS_TENTH_FRAME)