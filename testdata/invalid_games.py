"""invalid bowling game test data"""


# spare cannot be the first roll
SPARE_FIRST_ROLL = [
    ["/", "5"],
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


# invalid character not accepted in bowling
INVALID_SYMBOL = [
    ["A", "5"],
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


# too many rolls in 10th frame
TOO_MANY_ROLLS_TENTH_FRAME = [
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["5", "3", "7"],
]

# frame pin count  exceeds 10 without spare
FRAME_EXCEEDS_TEN = [
    ["8", "5"],
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


# extra frame after the game is complete
EXTRA_FRAME_AFTER_GAME = [
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X"],
    ["X", "X", "X"],
    ["5", "4"],
]



#below are not asked in PDF but are invalid games

# less than 10 frames
LESS_THAN_TEN_FRAMES = [
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


# more than 10 frames
MORE_THAN_TEN_FRAMES = [
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
    ["0", "0"],
]

# strike cannot appear as the second roll of a regular frame
INVALID_STRIKE_SECOND_ROLL = [
    ["5", "X"],
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

# four rolls in the tenth frame
FOUR_ROLLS_TENTH_FRAME = [
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["0", "0"],
    ["X", "X", "X", "X"],
]