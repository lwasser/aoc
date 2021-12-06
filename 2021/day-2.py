import os
import pandas as pd

data_path = "data-day-2.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
df = pd.read_csv(path, delim_whitespace=True, names=["direction", "amount"])

sumarised = df.groupby(["direction"]).sum().reset_index()
# Forward adds 5, down ads 5, up subtracts 5
depth = sumarised.amount.iloc[0] - sumarised.amount.iloc[2]
horizontal = sumarised.amount.iloc[1]

total = depth * horizontal

""" Challenge 2

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

"""

aim = 0
horizontal = 0
depth = 0
for index, row in df.iterrows():
    # Down X increases your aim by X units
    if row.direction == "down":
        aim += row.amount
    # Up X decreases your aim by X units
    elif row.direction == "up":
        aim -= row.amount
    # Forward - It increases your horizontal position by X units
    # increases your depth by your aim multiplied by X
    elif row.direction == "forward":
        depth += aim * row.amount
        horizontal += row.amount

final = horizontal * depth
print("The challenge 2 answer is", final)
