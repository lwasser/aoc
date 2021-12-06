"""Puzzle 1a"""
# Count the number of times a depth measurement increases

import os
import pandas as pd

data_path = "data-day-1.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)

# Read and cleanup
with open(path) as f:
    lines = f.readlines()

# Use lists
final_vals = [int(anum.strip()) for anum in lines]


# Clean list comprehension approach harder to read
len(
    [
        i
        for i in range(len(final_vals) - 1)
        if final_vals[i + 1] > final_vals[i]
    ]
)


def count_increase(vals):
    increase_only = [i for i in range(len(vals) - 1) if vals[i + 1] > vals[i]]
    return len(increase_only)


# 1292 correct
answer_a = count_increase(final_vals)
print("The part a answer is", answer_a)

"""Puzzle 1b"""

# Get and rolling sum
n = 3
rolling = pd.Series(final_vals).rolling(window=n).sum().dropna().to_list()
answer_b = count_increase(rolling)

len(
    [
        i
        for i in range(len(final_vals) - 3)
        if final_vals[i + 3] > final_vals[i]
    ]
)

# 1262 correct
print("The answer is", answer_b)
