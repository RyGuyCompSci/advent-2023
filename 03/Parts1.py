import re

def solution(filename):
    sum = 0
    file = open(filename, "r")
    lines = []
    for line in file:
        lines.append(line)
        print(re.findall(r"\d+", line))
        # print(line.split('.'))
        sum = sum + 0
    print(lines[0][0])
    file.close()
    return sum

filename = "test_input.txt"
print(solution(filename))


