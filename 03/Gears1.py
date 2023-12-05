"""
Given a set of lines, return the indices of all the non-numeric, newline, or period characters
"""
def get_symbols(lines):
    symbols = []
    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(0, len(line)):
            char = line[x]
            if not (char.isnumeric() or char == "." or char == "\n"):
                symbols.append((x, y))
    return symbols

"""
Given a coordinate, removes all adjacent entries to left and right of coordinate
"""
def remove_neighbors(coordinate, numbers):
    i = coordinate[0]
    j = coordinate[1] # always stays the same
    # remove coordinate
    del numbers[(i, j)]

    # remove lower
    i = coordinate[0] - 1
    while (i, j) in numbers:
        del numbers[(i, j)]
        i = i - 1

    # remove upper
    i = coordinate[0] + 1
    while (i, j) in numbers:
        del numbers[(i, j)]
        i = i + 1
    return numbers

"""
Given a coordinate, check all around it and see if an entry
exists in our numbers dict. If it does, record it's value and
remove it's neighbors from the nubmers dict (see remove_neighbors()).
"""
def check_coordinates(coordinate, numbers):
    val = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            new_coord = (coordinate[0] + i, coordinate[1] + j)
            if new_coord in numbers:
                val = val + numbers[new_coord][0]
                numbers = remove_neighbors(new_coord, numbers)
            j = j + 1
        i = i + 1
    return (val, numbers)


def solution(filename):
    sum = 0
    numbers = {}
    lines = []
    file = open(filename, "r")
    y = 0;
    for line in file:
        lines.append(line)
        x = 0
        while x < len(line) - 1:
            char = line[x]
            if char.isnumeric():
                # build up substring
                number = ""
                sub_index = 0
                while line[x + sub_index].isnumeric():
                    number = number + line[x + sub_index]
                    sub_index = sub_index + 1
                # add to other entries
                for i in range(0, len(number)):
                    numbers[(x + i, y)] = (int(number), i) # TODO: use index to remove adjacent values later
                x = x + len(number) # skip to end of number
            else:
                x = x + 1 # increment x
        y = y + 1 # increment y
    symbols = get_symbols(lines)
    for symbol in symbols:
        computed = check_coordinates(symbol, numbers)
        sum = sum + int(computed[0])
        numbers = computed[1]
    file.close()
    return sum

filename = "input.txt"
print(solution(filename))
