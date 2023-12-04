import re

def solution(filename):
  file = open(filename, "r")
  sum = 0

  for line in file:
    line = re.sub("([A-z])|(\n)", "", line)
    first = line[0]
    last = line[len(line) - 1]
    sum = sum + int(first + last)
  file.close()
  return sum


filename = "input.txt"
print(solution(filename))
