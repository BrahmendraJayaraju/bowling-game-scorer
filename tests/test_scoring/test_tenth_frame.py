"""
test different tenth frame scenarios
"""

import allure
import pytest
from src.engine.scorer import BowlingScorer
from testdata.valid_games import (
    TENTH_FRAME_STRIKE_SCORE,
    TENTH_FRAME_SPARE_SCORE,
    TENTH_FRAME_OPEN_SCORE,
)


@allure.feature("Bowling Scoring")
@allure.story("Tenth Frame")
@allure.title("Verify strike in the tenth frame")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(1)
def test_tenth_frame_strike(tenth_frame_strike):

    scorer = BowlingScorer()

    actual_score = scorer.score(tenth_frame_strike)

    assert actual_score[-1] == TENTH_FRAME_STRIKE_SCORE


@allure.feature("Bowling Scoring")
@allure.story("Tenth Frame")
@allure.title("Verify spare in the tenth frame")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(2)
def test_tenth_frame_spare(tenth_frame_spare):

    scorer = BowlingScorer()

    actual_score = scorer.score(tenth_frame_spare)

    assert actual_score[-1] == TENTH_FRAME_SPARE_SCORE

@pytest.mark.order(3)
@allure.feature("Bowling Scoring")
@allure.story("Tenth Frame")
@allure.title("Verify open tenth frame")
@allure.severity(allure.severity_level.CRITICAL)
def test_tenth_frame_open(tenth_frame_open):

    scorer = BowlingScorer()

    actual_score = scorer.score(tenth_frame_open)

    assert actual_score[-1] == TENTH_FRAME_OPEN_SCORE