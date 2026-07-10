"""testing a bowling game with all open frames
"""

from src.engine.scorer import BowlingScorer
from testdata.valid_games import ALL_OPEN_SCORE
import allure

@allure.feature("Bowling Scoring")
@allure.story("Open Frames")
@allure.title("Verify cumulative score for a game with all open frames")
@allure.severity(allure.severity_level.CRITICAL)
def test_all_open_frames(all_open):

    scorer = BowlingScorer()

    actual_score = scorer.score(all_open)

    assert actual_score == ALL_OPEN_SCORE