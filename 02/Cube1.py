import re

# Maximum number of blocks represented by a dictionary
color_dict = {"r": 12, "g": 13, "b": 14}


def flatten_hand(hand):
    hand = "::".join(hand.split(";"))
    return "::".join(hand.split(",")).split("::")


def check_game(line):
    game = line.split(":")
    game_id = re.search("\d+", game[0])[0]
    hand = flatten_hand(game[1])
    for cubes in hand:
        count = int(re.search(r"\d+", cubes)[0])
        color = re.search(r"\d+ \w", cubes)[0][-1::]
        if count > color_dict[color]:
            return 0  # exceeds limit, do not count game id
    return int(game_id)


def solution(filename):
    sum = 0
    file = open(filename, "r")
    for line in file:
        sum = sum + check_game(line)
    file.close()
    return sum


filename = "input.txt"
print(solution(filename))
