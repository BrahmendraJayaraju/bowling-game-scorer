"""testing the example game provided in the PDF
"""
from src.engine.scorer import BowlingScorer
from testdata.valid_games import EXAMPLE_GAME_SCORE
import allure

@allure.feature("Bowling Scoring")
@allure.story("Example Game")
@allure.title("Verify cumulative score for the example game")
@allure.severity(allure.severity_level.CRITICAL)
def test_example_game(example_game):

    scorer = BowlingScorer()

    actual_score = scorer.score(example_game)

    assert actual_score == EXAMPLE_GAME_SCORE