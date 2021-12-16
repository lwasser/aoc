import os
import copy
from heapq import heappop, heappush
import numpy as np

# data_path = "day-15-test.txt"
data_path = "day-15-data.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
with open(path) as f:
    risk_map = [line.strip() for line in f.readlines()]
    risk_map = [[int(achar) for achar in aline] for aline in risk_map]


def get_neighbor(r, c):
    """Return the neighbors assuming no diag movement"""
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def find_path(a_map):
    """Right now ths expects a list but can play with an array as well?"""
    r_final = len(a_map)
    c_final = len(a_map[0])
    # SET - Adding too a set is more efficient than appending to a list
    # why?
    locked = set()
    que = [(0, (0, 0))]
    while que:
        # This will always grab the smallest value so you don't have to find it
        risk, row_col = heappop(que)
        # If at the end of the matrix, stop.
        if row_col == (r_final - 1, c_final - 1):
            print("FINAL Destination!")
            break
        # If it's already in locked then you don't have to iterate through rows
        # and cols below - next.
        if row_col in locked:
            continue
        # If you want to retrace steps but likely not needed
        locked.add(row_col)
        # Now iterate through the neighbors
        for arow, acol in get_neighbor(*row_col):
            # This is a bit sloppy because you have values that are outside of
            # the elements in the array... must be a cleaner way
            if 0 <= arow < r_final and 0 <= acol < c_final:
                # Add to the queu - (new_risk, (r,c))
                heappush(que, (risk + a_map[arow][acol], (arow, acol)))
    return risk


final_risk_part1 = find_path(risk_map)
print("Part A: The final risk is:", final_risk_part1)

"""PART 2 - more data"""

#  deepcopy() for nested lists is the only way to properly copy
enlarged_rm = copy.deepcopy(risk_map)
enlarged_rm = np.array(enlarged_rm)

nrow = np.hstack(
    [
        enlarged_rm,
        enlarged_rm + 1,
        enlarged_rm + 2,
        enlarged_rm + 3,
        enlarged_rm + 4,
    ]
)
new_data = np.vstack([nrow, nrow + 1, nrow + 2, nrow + 3, nrow + 4])
# This provides the remainder of the division result. So 9 is the biggest
# number. Values bigger than 9 are thus reassigned
new_data %= 9
# There are no zeroes in this data - these should be 1's
new_data[new_data == 0] = 9

# I am sure I can do this with numpy but let's play with turning
# it back into a list
final_list = []
for i in range(new_data.shape[0]):
    final_list.append(list(new_data[i]))

final_risk_part2 = find_path(final_list)
print("Part B: The final risk is", final_risk_part2)
