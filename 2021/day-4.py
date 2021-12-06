import os
import numpy as np
import time

# This approach is brittle because i'm replacing values in the original arr
# really should do this in a function to avoid messing with the original data

# Use the test data or not
test = False
if test:
    data_path = "test-day-4-bingo.txt"
    data_path_b = "test-day-4.txt"
    reshape_val = 3
else:
    data_path = "data-day-4.txt"
    data_path_b = "data-day-4b.txt"
    reshape_val = 100
path = os.path.join(os.getcwd(), "2021", "data", data_path)
pathb = os.path.join(os.getcwd(), "2021", "data", data_path_b)

# Read and cleanup
with open(pathb) as f:
    lines = f.readlines()[0].split(",")

bingo_vals = [int(i) for i in lines]


def check_for_bingo(arr, mask_val):
    """Test for bingo in both directions"""
    ax = np.all(arr == mask_val, axis=0)
    ax1 = np.all(arr == mask_val, axis=1)
    # not sure if this works as i would expect but seems to be working
    if any(ax) or any(ax1):
        return True
    else:
        return False


# Getin' my numpy on
arr = np.loadtxt(path, ndmin=2, dtype="int")
# Test data has 3
arr_bingo = np.reshape(arr, (reshape_val, 5, 5))
test_bkp = arr_bingo.copy()

mask = -99
finish = False
for i, aval in enumerate(bingo_vals):
    # This is ugly
    if not finish:
        # First mask all values in the array to -99
        arr_bingo = np.where(arr_bingo == aval, mask, arr_bingo)
        # check for bingo
        for index, an_arr in enumerate(arr_bingo):
            if check_for_bingo(an_arr, mask):
                print("BINGO BITCHES!", aval)
                final_bingo = an_arr
                final_val = aval
                finish = True
                break
    else:
        break

# Sum of all unmarked numbers
sum = final_bingo[(final_bingo > 0)].sum()
final_value = sum * final_val
# Answer is 11536
print("The final answer is - I win, SQUID", final_value)


"""Part b
Here, the last board wins vs the first board to win... let the damn
squid win. squids are cute so why not?

"""


t0 = time.time()

# Getin' my numpy on
arr = np.loadtxt(path, ndmin=2, dtype="int")
# Test data has 3
arr_bingo = np.reshape(arr, (reshape_val, 5, 5))

mask = -99
last_bingo = False
arr_bingo_play = arr_bingo.copy()
for i, aval in enumerate(bingo_vals):
    all_slices = []
    if last_bingo:
        break
    else:
        # First mask all values in the array to -99
        arr_bingo_play = np.where(arr_bingo_play == aval, mask, arr_bingo_play)
        for index, an_arr in enumerate(arr_bingo_play):
            if check_for_bingo(an_arr, mask):
                # Note i could pull the arr when it hits bingo because extra
                # processing is happening here too but... maybe later or never
                print("BINGO BITCHES!", aval)
                # Populate remove slices list
                all_slices.append(index)
                if arr_bingo_play.shape[0] == 1:
                    print("All Done")
                    last_bingo = True
                    final_val = aval
                    break
        if arr_bingo_play.shape[0] > 1:
            # Remove boards that already have bingo before starting next
            # Cause extra processing is icky
            arr_bingo_play = np.delete(arr_bingo_play, all_slices, axis=0)

# Sum of all unmarked numbers
sum = arr_bingo_play[(arr_bingo_play > 0)].sum()
print("Sum is", sum, "Val is", final_val)
final_value = sum * final_val
# 1284 is correct
print("Final value is", final_value)

t1 = time.time()
t1 - t0
