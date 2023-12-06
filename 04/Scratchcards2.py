import re


def get_score(line):
    winners = line.split(" | ")[0].split(" ")
    numbers = line.split(" | ")[1].split(" ")
    num_wins = len([val for val in numbers if val in winners])
    return num_wins


def play_game(games):
    score = get_score(games[0])
    for i in range(0, score):
        score = score + play_game(games[i + 1 :])
    return score


def cleanup(line):
    line = re.sub(r"(Card \d+: )|(\n)", "", line)
    line = re.sub(r"\s\s", " ", line)
    return line


def solution(filename):
    games = []
    file = open(filename, "r")
    sum = 0
    for line in file:
        line = cleanup(line)
        games.append(line)
    for i in range(0, len(games)):
        sum = sum + play_game(games[i:])
    file.close()
    return sum + len(games)


filename = "input.txt"
print(solution(filename))
