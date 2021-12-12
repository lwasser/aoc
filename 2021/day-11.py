"""
You can model the energy levels and flashes of light in steps.
During a single step, the following occurs:

* First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This
increases the energy level of all adjacent octopuses by 1, including
octopuses that are diagonally adjacent.
 If this causes an octopus to have an energy level greater than 9,
 it also flashes. This process continues as long as new octopuses keep having
 their energy level increased beyond 9. (An octopus can only flash at most
 once per step.)
Finally, any octopus that flashed during this step has its energy level set
to 0, as it used all of its energy to flash.
"""

import os
import numpy as np

data_path = "day-11-test.txt"
data_path = "day-11-data.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
with open(path) as f:
    all_data = [line.strip() for line in f.readlines()]

all_ints = [[int(i) for i in d] for d in all_data]
all_ints_ar = np.array(all_ints)


def create_window(x, y, shape):
    """returns window of array"""
    # Create window (turn into helper)
    if x == 0:
        x_start = None
    else:
        x_start = x - 1
    if y == 0:
        y_start = None
    else:
        y_start = y - 1
    # Will need to account for edges here too
    if x == shape[1]:
        x_end = None
    else:
        x_end = x + 2
    if y == shape[0]:
        y_end = None
    else:
        y_end = y + 2
    return x_start, x_end, y_start, y_end


work_arr = all_ints_ar.copy()
total_flashes = 0
total_steps = 100
for a_step in range(total_steps):
    # Step 1 - all values increase by 1
    work_arr = work_arr + 1
    # Now count subsequent flashes  - increase the energy level of all
    # adjacent vals by 1
    # This step continues until there are no more 9s in the arr
    while 10 in work_arr:
        indices = (work_arr == 10).nonzero()
        index = 0
        for x, y in zip(indices[0], indices[1]):
            index += 1
            # Create window
            x_start, x_end, y_start, y_end = create_window(
                x, y, work_arr.shape
            )
            window_update = work_arr[x_start:x_end, y_start:y_end]
            # Values of 9 should become 10 and 10 should remain 10
            window_update[(window_update > 8) & (window_update < 11)] = 10
            # Everything else +1
            window_update[window_update < 9] += 1
            # Update values following rules above
            work_arr[x_start:x_end, y_start:y_end] = window_update
            # Index should be 11
            work_arr[x, y] = 9999

    # When this is done reset all values > 9 to 0
    work_arr = np.where(work_arr > 9, 0, work_arr)
    # Count new flashes (== 10)
    total_flashes += len(work_arr[work_arr == 0])
# 1743
print("TOTAL Flashes part a", total_flashes)

""" PART B"""

work_arr = all_ints_ar.copy()
step = 0
while not np.all((work_arr == 0)):
    step += 1
    # Step 1 - all values increase by 1
    work_arr = work_arr + 1
    # Now count subsequent flashes  - increase the energy level of all
    # adjacent vals by 1
    # This step continues until there are no more 9s in the arr
    while 10 in work_arr:
        indices = (work_arr == 10).nonzero()
        index = 0
        for x, y in zip(indices[0], indices[1]):
            index += 1
            # Create window
            x_start, x_end, y_start, y_end = create_window(
                x, y, work_arr.shape
            )
            window_update = work_arr[x_start:x_end, y_start:y_end]
            window_update[(window_update > 8) & (window_update < 11)] = 10
            window_update[window_update < 9] += 1
            # Update values following rules above
            work_arr[x_start:x_end, y_start:y_end] = window_update
            # Index should be 11
            work_arr[x, y] = 9999

    # When this is done reset all values > 9 to 0
    work_arr = np.where(work_arr > 9, 0, work_arr)

# 364
print("Final steps - part b", step)
