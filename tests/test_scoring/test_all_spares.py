"""test a bowling game with all spares"""

from src.engine.scorer import BowlingScorer
from testdata.valid_games import ALL_SPARES_SCORE
import allure

@allure.feature("Bowling Scoring")
@allure.story("All Spares")
@allure.title("Verify cumulative score for a game with all spares")
@allure.severity(allure.severity_level.CRITICAL)
def test_all_spares(all_spares):

    scorer = BowlingScorer()

    actual_score = scorer.score(all_spares)

    assert actual_score == ALL_SPARES_SCORE