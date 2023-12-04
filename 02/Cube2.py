import re


def flatten_hand(hand):
    hand = "::".join(hand.split(";"))
    return "::".join(hand.split(",")).split("::")


def check_game(line):
    color_dict = {"r": 0, "g": 0, "b": 0}
    game = line.split(":")
    hand = flatten_hand(game[1])
    for colors in hand:
        count = int(re.search(r"\d+", colors)[0])
        color = re.search(r"\d+ \w", colors)[0][-1::]
        color_dict[color] = max(color_dict[color], count)
    return color_dict["r"] * color_dict["g"] * color_dict["b"]


def solution(filename):
    sum = 0
    file = open(filename, "r")
    for line in file:
        sum = sum + check_game(line)
    file.close()
    return sum


filename = "input.txt"
print(solution(filename))
