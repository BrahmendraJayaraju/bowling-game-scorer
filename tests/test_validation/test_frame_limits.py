"""
testing game with  frame count validation
"""
import allure
import pytest
from src.engine.scorer import BowlingScorer
from src.exceptions.bowling_exceptions import InvalidFrameCountError


@allure.feature("Validation")
@allure.story("Frame Count")
@allure.title("Verify exception is raised when game has less than 10 frames")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(1)
def test_less_than_ten_frames(less_than_ten_frames):

    scorer = BowlingScorer()

    with pytest.raises(InvalidFrameCountError):
        scorer.score(less_than_ten_frames)


@allure.feature("Validation")
@allure.story("Frame Count")
@allure.title("Verify exception is raised when game has more than 10 frames")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(2)
def test_more_than_ten_frames(more_than_ten_frames):

    scorer = BowlingScorer()

    with pytest.raises(InvalidFrameCountError):
        scorer.score(more_than_ten_frames)