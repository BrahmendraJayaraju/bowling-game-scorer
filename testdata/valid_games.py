"""valid bowling game test data"""

# example game which is  provided in  PDF
EXAMPLE_GAME = [
    ["8", "/"],
    ["5", "4"],
    ["9", "0"],
    ["X"],
    ["X"],
    ["5", "/"],
    ["5", "3"],
    ["6", "3"],
    ["9", "/"],
    ["9", "/", "X"],
]

EXAMPLE_GAME_SCORE = [15, 24, 33, 58, 78, 93, 101, 110, 129, 149]


# perfect game(12 strikes) returns 300
PERFECT_GAME = [
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X", "X","X"],
]

PERFECT_GAME_SCORE = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]


# all spares(e.g., 5/ in frames 1–10 with a 5 bonus) returns 150
ALL_SPARES = [
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/"],
    ["5", "/", "5"],
]

ALL_SPARES_SCORE = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]


# all open frames(no strikes/spares) returns the correct total
ALL_OPEN = [
    ["3", "5"],
    ["2", "4"],
    ["6", "1"],
    ["4", "3"],
    ["5", "2"],
    ["8", "1"],
    ["2", "5"],
    ["6", "2"],
    ["1", "7"],
    ["3", "4"],
]

ALL_OPEN_SCORE = [8, 14, 21, 28, 35, 44, 51, 59, 67, 74]





# tenth frame ->  strike + two bonus rolls
TENTH_FRAME_STRIKE = [
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["X", "5", "4"],
]

TENTH_FRAME_STRIKE_SCORE = 19


# tenth frame -> spare + one bonus roll
TENTH_FRAME_SPARE = [
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["5", "/", "8"],
]

TENTH_FRAME_SPARE_SCORE = 18


# tenth frame -> open frame ends the game (no bonus)
TENTH_FRAME_OPEN = [
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["5", "3"],
]

TENTH_FRAME_OPEN_SCORE = 8


# gutter game (not in pdf)
GUTTER_GAME = [
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
]

GUTTER_GAME_SCORE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]