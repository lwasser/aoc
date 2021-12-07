"""
All hail the lanterfish

# model each fish as a single number that represents the number of days
# until it creates a new lanternfish.

# RULES
each lanternfish creates a new lanternfish once every 7 days
A new lanternfish needs two more days for its first cycle.

suppose you have a lanternfish with an internal timer value of 3:
# RULE Interval decreases by 1 day.
# 4 days it creates a new fish and resets to 6
# After one day, its internal timer would become 2.
# After another day, its internal timer would become 1.
# After another day, its internal timer would become 0.
# After another day, its internal timer would reset to 6, and it would create a
 new lanternfish with an internal timer of 8.
After another day, the first lanternfish would have an internal timer of 5,
and the second lanternfish would have an internal timer of 7.

* lanternfish that creates a new fish resets its timer to 6
* a new lanternfish starts with an internal timer of 8 and does not start
  counting down until the next day.

Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each
other number decreases by 1 if it was present at the start of the day.
"""

import numpy as np

# Fish and their interview timers
test_fishies = [3, 4, 3, 1, 2]
# The real data
test_fishies = [
    3,
    5,
    1,
    5,
    3,
    2,
    1,
    3,
    4,
    2,
    5,
    1,
    3,
    3,
    2,
    5,
    1,
    3,
    1,
    5,
    5,
    1,
    1,
    1,
    2,
    4,
    1,
    4,
    5,
    2,
    1,
    2,
    4,
    3,
    1,
    2,
    3,
    4,
    3,
    4,
    4,
    5,
    1,
    1,
    1,
    1,
    5,
    5,
    3,
    4,
    4,
    4,
    5,
    3,
    4,
    1,
    4,
    3,
    3,
    2,
    1,
    1,
    3,
    3,
    3,
    2,
    1,
    3,
    5,
    2,
    3,
    4,
    2,
    5,
    4,
    5,
    4,
    4,
    2,
    2,
    3,
    3,
    3,
    3,
    5,
    4,
    2,
    3,
    1,
    2,
    1,
    1,
    2,
    2,
    5,
    1,
    1,
    4,
    1,
    5,
    3,
    2,
    1,
    4,
    1,
    5,
    1,
    4,
    5,
    2,
    1,
    1,
    1,
    4,
    5,
    4,
    2,
    4,
    5,
    4,
    2,
    4,
    4,
    1,
    1,
    2,
    2,
    1,
    1,
    2,
    3,
    3,
    2,
    5,
    2,
    1,
    1,
    2,
    1,
    1,
    1,
    3,
    2,
    3,
    1,
    5,
    4,
    5,
    3,
    3,
    2,
    1,
    1,
    1,
    3,
    5,
    1,
    1,
    4,
    4,
    5,
    4,
    3,
    3,
    3,
    3,
    2,
    4,
    5,
    2,
    1,
    1,
    1,
    4,
    2,
    4,
    2,
    2,
    5,
    5,
    5,
    4,
    1,
    1,
    5,
    1,
    5,
    2,
    1,
    3,
    3,
    2,
    5,
    2,
    1,
    2,
    4,
    3,
    3,
    1,
    5,
    4,
    1,
    1,
    1,
    4,
    2,
    5,
    5,
    4,
    4,
    3,
    4,
    3,
    1,
    5,
    5,
    2,
    5,
    4,
    2,
    3,
    4,
    1,
    1,
    4,
    4,
    3,
    4,
    1,
    3,
    4,
    1,
    1,
    4,
    3,
    2,
    2,
    5,
    3,
    1,
    4,
    4,
    4,
    1,
    3,
    4,
    3,
    1,
    5,
    3,
    3,
    5,
    5,
    4,
    4,
    1,
    2,
    4,
    2,
    2,
    3,
    1,
    1,
    4,
    5,
    3,
    1,
    1,
    1,
    1,
    3,
    5,
    4,
    1,
    1,
    2,
    1,
    1,
    2,
    1,
    2,
    3,
    1,
    1,
    3,
    2,
    2,
    5,
    5,
    1,
    5,
    5,
    1,
    4,
    4,
    3,
    5,
    4,
    4,
]

current_fish_age = [6 - i for i in test_fishies]

# Mature every 7 days, immature every 9
current_count = [0] * 7
# Count values in initial list
for age in current_fish_age:
    current_count[age] += 1

count_mature = np.array(current_count)
count_immature = np.array([0] * 9)
# short at day 11 there should be 15 after this day
total_days = 256
# Could turn this into a get_fish function and reduce code
new_mature, new_immature = 0, 0
for day in range(total_days):  # range(total_days):
    # Move up a step for each day
    count_immature = np.roll(count_immature, 1)
    count_mature = np.roll(count_mature, 1)
    # Add new fishies
    count_mature[0] += new_mature
    count_immature[0] += new_immature
    if count_immature[len(count_immature) - 1] > 0:
        print("make new mature fish")
        new_mature = count_immature[len(count_immature) - 1]
        print("new mature", new_mature)
    else:
        new_mature = 0
    if count_mature[len(count_mature) - 1] > 0:
        print("make new baby fish")
        new_immature = count_mature[len(count_mature) - 1]
        print("new immature", new_immature)
    else:
        new_immature = 0

# How many fishies do we have now?
# 351188 - 80 days
# 1595779846729 256 days
print("We have", sum(count_immature) + sum(count_mature), "Fishies")


# Old code - not efficient
# fish_parta = test_fishies.copy()
# n = 18
# for aday in range(n):
#     # Function maybe? - can you map list values?
#     day_ls = []
#     birth = []
#
#     for afish in fish_parta:
#         if afish == 0:
#             day_ls.append(6)
#             birth.append(8)
#         else:
#             day_ls.append(afish-1)
#     print("day", aday, "birth", birth)
#     fish_parta = day_ls + birth
# # 351188
# print("Total Fishies", len(fish_parta))

# Init dict

# Convert to ages so counting up which makes my brain hurt less
# current_fish_age = []
# for i in test_fishies:
#     current_fish_age.append(6 - i)
