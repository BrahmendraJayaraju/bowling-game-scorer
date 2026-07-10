import allure
from src.engine.scorer import BowlingScorer
import pytest
from src.exceptions.bowling_exceptions import InvalidSymbolError

"""
testing invalid roll symbols
"""

@allure.feature("Validation")
@allure.story("Invalid Symbol")
@allure.title("Verify exception is raised for an invalid roll symbol")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_symbol(invalid_symbol):

    scorer = BowlingScorer()

    with pytest.raises(InvalidSymbolError):
        scorer.score(invalid_symbol)