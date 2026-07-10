"""
testing invalid frame scenarios
"""
from src.engine.scorer import BowlingScorer
from src.exceptions.bowling_exceptions import *
import allure
import pytest

@allure.feature("Validation")
@allure.story("Invalid Frame")
@allure.title("Verify exception is raised when spare is the first roll")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(1)
def test_spare_first_roll(spare_first_roll):

    scorer = BowlingScorer()

    with pytest.raises(InvalidRollError):
        scorer.score(spare_first_roll)


@allure.feature("Validation")
@allure.story("Invalid Frame")
@allure.title("Verify exception is raised when frame pin count exceeds 10")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(2)
def test_frame_exceeds_ten(frame_exceeds_ten):

    scorer = BowlingScorer()
    with pytest.raises(InvalidFrameError):
        scorer.score(frame_exceeds_ten)

@allure.feature("Validation")
@allure.story("Invalid Frame")
@allure.title("Verify exception is raised when strike is used as the second roll")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(3)
def test_invalid_strike_second_roll(invalid_strike_second_roll):

    scorer = BowlingScorer()

    with pytest.raises(InvalidRollError):
        scorer.score(invalid_strike_second_roll)


@allure.feature("Validation")
@allure.story("Invalid Frame")
@allure.title("Verify exception is raised when four rolls are provided in the 10th frame")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(4)
def test_four_rolls_in_tenth_frame(four_rolls_tenth_frame):

    scorer = BowlingScorer()

    with pytest.raises(InvalidFrameError):
        scorer.score(four_rolls_tenth_frame)