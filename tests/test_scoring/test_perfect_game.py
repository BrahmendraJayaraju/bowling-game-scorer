"""
test a perfect bowling game
"""
import allure
from src.engine.scorer import BowlingScorer
from testdata.valid_games import PERFECT_GAME_SCORE


@allure.feature("Bowling Scoring")
@allure.story("Perfect Game")
@allure.title("Verify cumulative score for a perfect game")
@allure.severity(allure.severity_level.CRITICAL)
def test_perfect_game(perfect_game):

    scorer = BowlingScorer()

    actual_score = scorer.score(perfect_game)

    assert actual_score == PERFECT_GAME_SCORE