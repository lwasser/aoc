import os
import numpy as np

data_path = "data-day-5-test.txt"
data_path = "day-5-data.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)

data = []
# Read and cleanup
with open(path) as f:
    for line in f.readlines():
        data.append(line.split())

# Data are strings rather than numbers.
# Drop that goofy ->
cleaned_data = [[i[0], i[2]] for i in data]
# Split and turn into numbers for indexing later
# This is hideous data cleaning but moving on for now
new_list = []
for data in cleaned_data:
    new_list.append(data[0].split(",") + data[1].split(","))

final_list = []
diagnol_list = []
# Throw out data where either x1 != x2 or y1 != y2
for lst in new_list:
    if lst[0] == lst[2] or lst[1] == lst[3]:
        final_list.append(list(map(int, lst)))
    else:
        diagnol_list.append(list(map(int, lst)))


# Note test data does start at 0, don't think my actual data does so will
# need to adjust by min value
# only consider horizontal and vertical lines
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
    location_map[starty:endy, startx:endx] = (
        location_map[starty:endy, startx:endx] + 1
    )

# At how many points do at least two lines overlap?
# 7297
location_map[location_map >= 2].shape[0]


"""part b

I knew it - consider diagnols too this means slicing wont work
"""

# This contains all coordinates
max_val = int(np.max(np.array(final_list)))
min_val = int(np.min(np.array(final_list)))
shape = np.array(final_list).shape
arr_shape = max_val - min_val
# The shape shouldn't matter in theory
location_map = np.zeros((max_val + 1, max_val + 1), dtype="int")

# Process the hor / vert lines
for alist in final_list:
    startx, starty, endx, endy = get_index(alist)
    location_map[starty:endy, startx:endx] = (
        location_map[starty:endy, startx:endx] + 1
    )

for alist in diagnol_list:
    startx, starty, endx, endy = alist
    total_steps = abs(startx - endx) + 1
    print("LOOP", alist)
    y, x = starty, startx
    for i in range(total_steps):
        print("iter", i, "next coord:", x, y)
        location_map[y, x] = location_map[y, x] + 1
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
location_map[location_map >= 2].shape[0]
