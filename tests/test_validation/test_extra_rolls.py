"""
test extra roll validation scenarios
"""



from src.engine.scorer import BowlingScorer
from src.exceptions.bowling_exceptions import *

import allure
import pytest

@allure.feature("Validation")
@allure.story("Extra Rolls")
@allure.title("Verify exception is raised for too many rolls in the 10th frame")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(1)
def test_too_many_rolls_in_tenth_frame(too_many_rolls_tenth_frame):

    scorer = BowlingScorer()

    with pytest.raises(InvalidFrameError):
        scorer.score(too_many_rolls_tenth_frame)


@allure.feature("Validation")
@allure.story("Extra Rolls")
@allure.title("Verify exception is raised for extra rolls after game completion")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(2)
def test_extra_roll_after_game(extra_roll_after_game):

    scorer = BowlingScorer()

    with pytest.raises(InvalidFrameCountError):
        scorer.score(extra_roll_after_game)