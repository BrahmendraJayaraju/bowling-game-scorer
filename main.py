"""sample program to run the Bowling Game Scorer
(you can run all  Test cases  in git actions i have done configuration of CI/CD pipeline in github actions refer Readme.md for more details its in ending )"""

from src.engine.parser import GameParser
from src.engine.scorer import BowlingScorer

from testdata.valid_games import EXAMPLE_GAME


def main():
    game = GameParser.parse(EXAMPLE_GAME)

    scorer = BowlingScorer()

    cumulative_scores = scorer.score(game)

    print("cumulative scores:")

    for frame_number, score in enumerate(cumulative_scores, start=1):
        print(f"frame {frame_number}: {score}")


if __name__ == "__main__":
    main()