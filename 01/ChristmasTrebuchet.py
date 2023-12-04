import re

file_name = "input.txt"

def get_file(name):
  return open(name, "r")

def solution():
  file = get_file(file_name)
  sum = 0

  for line in file:
    line = re.sub("([A-z])|(\n)", "", line)
    first = line[0]
    last = line[len(line) - 1]
    sum = sum + int(first + last)
  file.close()
  return sum


print(solution())
