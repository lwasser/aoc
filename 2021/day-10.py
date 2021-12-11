import os

data_path = "day-10-test.txt"
data_path = "day-10.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
with open(path) as f:
    all_data = [line.strip() for line in f.readlines()]

# Illegal char lookup
lookup = {")": [3], "]": [57], "}": [1197], ">": [25137]}

# Keys are the opening brackets
bracket_lookup = {"[": "]", "{": "}", "(": ")", "<": ">"}

# Got help with this part - this is much more efficient
points = 0
# Part 1
for astr in all_data:
    open_brackets = []
    for achar in astr:
        print(achar)
        # If the character is in dict keys (opening char), append
        if achar in bracket_lookup.keys():
            open_brackets.append(achar)
            print("Stack appending", open_brackets)
        # If there's a matching closing element, remove from list
        elif achar == bracket_lookup[open_brackets[-1]]:
            # Remove from the list if there is a matching char
            print("Stack removing", open_brackets)
            open_brackets.pop()
        # This is a bit brittle - could nest another if else above
        elif achar in bracket_lookup.values():
            print("Corrupt calculating points", open_brackets)
            points += lookup[achar][0]
            break
# ANSWER 392043
print("The total points are", points)


"""Part b"""

# Closing points dict
closing_points = {")": 1, "]": 2, "}": 3, ">": 4}

points = 0
incomplete = []
print("JUST STARTING OUT")
cor = []
final_points = []
# If i wanted to get the exact strings in the future enumerate is useful
# I don't need that but it's useful for troubleshooting
for index, astr in enumerate(all_data):
    open_brackets = []
    corrupted = False
    for achar in astr:
        # If the character is in dict keys (opening char), append
        if achar in bracket_lookup.keys():
            open_brackets.append(achar)
        # If there's a matching closing element, remove from list
        elif achar == bracket_lookup[open_brackets[-1]]:
            # Remove from the list if there is a matching char
            open_brackets.pop()
        # Here if qclosing bracket then line is corrupted
        elif achar in bracket_lookup.values():
            print("Corrupted")
            # No need to continue processing corrupted lines
            corrupted = True
            # If i want a list of incompletes this would do it
            # Don't actually need it for this problem
            cor.append(index)
            break
    if not corrupted:
        points = 0
        while open_brackets:
            char = open_brackets.pop()
            # Get the closing bracket
            key = bracket_lookup[char]
            # Multiple points by 5
            points *= 5
            points += closing_points[key]
        # Keep track of score
        final_points.append(points)

# Calculate final score
final_points.sort()
middle = int((len(final_points) - 1) / 2)
print("The total points are", final_points[middle])
