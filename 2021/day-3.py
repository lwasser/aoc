"""finding the most common bit in the corresponding position of all numbers
in the diagnostic report"""

# Setup
import os
import numpy as np

data_path = "data-day-3.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)

# Read and cleanup
with open(path) as f:
    lines = f.readlines()

# Clean data
final_vals = [anum.strip() for anum in lines]

# Second better way to populate array
arr_ls = []
for anindex, aval in enumerate(final_vals):
    arr_ls.append(np.reshape(np.fromiter(aval, "uint8"), (12, 1)))

a = np.hstack(arr_ls)


# Get counts
gamma = []
epsilon = []
for aval in range(a.shape[0]):
    unique, counts = np.unique(a[aval], return_counts=True)
    # Is 0 or 1 more common?
    if counts[0] > counts[1]:
        gamma.insert(len(gamma), 0)
        epsilon.insert(len(epsilon), 1)
    else:
        gamma.insert(len(gamma), 1)
        epsilon.insert(len(epsilon), 0)

# Turn values in list into single numbers via binary -> int
gamma_value = int("".join(map(str, gamma)), 2)
# Because this starts with a 0... can't use int
epsilon_value = int("".join(map(str, epsilon)), 2)

final = gamma_value * epsilon_value
# 3148794 should be correct
print("Final Value part A: ", final)


"""
part 2 - this aint pretty at 4am but it's working

Verify the life support rating, which can be determined by
multiplying the oxygen generator rating by the CO2 scrubber rating

What planet am i living on?

Start with all 12 numbers and consider only the first bit of each number.
There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with
a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits
(4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second
position: 10110, 10111, 10101, and 10000.
"""


def parse_arr(arr, position):
    """
    pos : tuple
        position... 01 or 10
    """
    for aval in range(arr.shape[0]):
        # Stop when one col is left
        if arr.shape[1] == 1:
            print("We're done now, thanks for playin'")
            break
        else:
            unique, counts = np.unique(arr[aval], return_counts=True)
            # If 0's are more common than 1's
            if counts[0] > counts[1]:
                # Slice out only columns that start with zero and replace array
                arr = arr[:, arr[aval] == position[0]]
                # Keep only numbers with 1 in the first position
                # Delete columns that start with one
            else:
                # Otherwise keep 1s instead
                arr = arr[:, arr[aval] == position[1]]
    # Return final array
    return arr


def list_to_binary_int(arr):
    arr_ls = arr.astype("int").astype("str").tolist()
    list_flat = [item for sublist in arr_ls for item in sublist]
    return int("".join(map(str, list_flat)), 2)


# Start fresh with new data just in case
all_vals_oxygen_arr = a.copy()
all_vals_co2_arr = a.copy()

# Calculate Oxygen
oxygen = parse_arr(all_vals_oxygen_arr, position=(0, 1))
final_o2 = list_to_binary_int(oxygen)

# Calculate Co2
co2 = parse_arr(all_vals_co2_arr, position=(1, 0))
final_co2 = list_to_binary_int(co2)

final_val = final_co2 * final_o2
# 2795310
print("The final is", final_val)
