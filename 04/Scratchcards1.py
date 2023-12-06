import re


def get_score(line):
    winners = line.split(" | ")[0].split(" ")
    numbers = line.split(" | ")[1].split(" ")
    wins = [val for val in numbers if val in winners]
    return 0 if len(wins) == 0 else 2 ** (len(wins) - 1)


def cleanup(line):
    line = re.sub(r"\s\s", " ", line)
    line = re.sub(r"(Card \d+: )|(\n)", "", line)
    return line


def solution(filename):
    file = open(filename, "r")
    sum = 0
    for line in file:
        line = cleanup(line)
        sum = sum + get_score(line)
    file.close()
    return sum


filename = "input.txt"
print(solution(filename))
