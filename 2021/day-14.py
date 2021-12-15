"""
import collections - collections.Counter could be a more efficient way to
count pairs and new letters.

"""

import os
from collections import Counter

# data_path = "day-14-test.txt"
data_path = "day-14-data.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
with open(path) as f:
    all_data = [line.strip().split(" ") for line in f.readlines()]

# Create dictionary of patterns and counts to track
code_map = {}
# fmt: off
for aline in all_data[2: len(all_data)]:
    code_map[aline[0]] = aline[2]
# fmt: off
start_template = all_data[0][0]
# Count letters in template object and populate count dict
letter_counts = Counter(start_template)


# SETUP Insert pairs into clean dict with pair: count_pair
def get_pairs(astring):
    """Takes a string and returns all pairs found in the string"""
    adict = Counter()
    for i in range(len(astring) - 1):
        pair = str(astring[i] + astring[i + 1])
        adict[pair] += 1
    return adict


# Update & reset counts
list_o_counts = get_pairs(start_template)
iteration = 0
steps = 40
while iteration < steps:
    iteration += 1
    new_dict = Counter()
    for akey in list_o_counts.keys():
        new_letter = code_map[akey]
        # Add letter to letter count
        pair_count = list_o_counts[akey]
        letter_counts[new_letter] += pair_count
        # Generate new pairs
        pair1 = akey[0] + new_letter
        pair2 = new_letter + akey[1]
        # TODO: Make this a little helper
        new_dict[pair1] += pair_count
        new_dict[pair2] += pair_count
    list_o_counts = new_dict.copy()

# Find most and least common letters
# Answer for 10 steps 2509
# Answer for 40 steps 2827627697643
print(
    "The final value is",
    max(letter_counts.values()) - min(letter_counts.values()),
)
