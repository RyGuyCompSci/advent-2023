import re

# attempts to parse line as a number
def convert_words_to_nums(line):
  sub_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
  }

  # iterate over keys to see if they exist in the string
  for key in sub_dict:
    if re.search(key, line) != None:
      line = re.sub(key, sub_dict[key], line)
      break # short-circuit after we find a match
  line = re.sub("([A-z])|(\n)", "", line) # remove extra alpha characters
  return int(line)

# return number from string
def get_number_from_string(line, backwards = False):
  num = ""
  # iterate
  for c in line:
    try: # check if our current character is a number, if so, return
      return int(c)
    except: # not a number, parse as string
      if backwards:
        num = c + num
      else:
        num = num + c
      try: # attempt to return the parsed number
        return convert_words_to_nums(num)
      except: # otherwise keep building the string
        continue
  return 0 # base case, should never get here

def solution(filename):
  file = open(filename, "r")
  sum = 0
  for line in file:
    first = str(get_number_from_string(line))
    last = str(get_number_from_string(line[::-1], True))
    sum = sum + int(first + last)
  file.close()
  return sum

filename = "input.txt"
print(solution(filename))
