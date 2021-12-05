import os
import numpy as np

data_path = "data-day-5-test.txt"
data_path = "day-5-data.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)

data = []
# Read and cleanup
with open(path) as f:
    for line in f.readlines():
        data.append(line.split()[0].split(",") + line.split()[2].split(","))
# String -> int
data_int = [list(map(int, lst)) for lst in data]

final_list = []
diagnol_list = []
for lst in data_int:
    # If the data only contain horizontal lines
    if lst[0] == lst[2] or lst[1] == lst[3]:
        final_list.append(lst)
    else:
        # List o' diagonals
        diagnol_list.append(lst)

max_val = int(np.max(np.array(final_list)))
min_val = int(np.min(np.array(final_list)))
shape = np.array(final_list).shape
arr_shape = max_val - min_val

""" Part A"""


def get_index(coord_list):
    """Sometimes the start and end are not in the expected order"""
    # First compare x's and make sure the smallest is first
    x1, y1, x2, y2 = alist
    if x1 > x2:
        startx, endx = x2, x1
    else:
        startx, endx = x1, x2
    if y1 > y2:
        starty, endy = y2, y1
    else:
        starty, endy = y1, y2
    return startx, starty, endx + 1, endy + 1


# Populate array with zeros
location_map = np.zeros((arr_shape + 1, arr_shape + 1), dtype="int")

for alist in final_list:
    startx, starty, endx, endy = get_index(alist)
    location_map[starty:endy, startx:endx] += 1

# At how many points do at least two lines overlap?
# 7297
print("Part A Answer", location_map[location_map >= 2].shape[0])


"""part b

I knew it - consider diagnols too this means slicing wont work
"""

# The shape shouldn't matter in theory
location_map = np.zeros((max_val + 1, max_val + 1), dtype="int")

# Process the hor / vert lines
for alist in final_list:
    startx, starty, endx, endy = get_index(alist)
    location_map[starty:endy, startx:endx] += 1

for alist in diagnol_list:
    startx, starty, endx, endy = alist
    total_steps = abs(startx - endx) + 1
    y, x = starty, startx
    for i in range(total_steps):
        location_map[y, x] += 1
        # Subtract x if the end is smaller than beginning
        if startx > endx:
            x -= 1
        else:
            x += 1
        if starty > endy:
            y -= 1
        else:
            y += 1
        total_steps += 1

# At how many points do at least two lines overlap?
# 21038
print("Part b answer: ", location_map[location_map >= 2].shape[0])
