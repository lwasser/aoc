import os

# test data
crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

data_path = "data-day-7.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
with open(path) as f:
    all_data = f.readlines()[0].split(",")
# Coerce to int
crab_positions = [int(data) for data in all_data]

# Dale says: Map the input numbers to ascii (anything in the valid ascii
# range -- basically 32 to 126).

secret_decoder_ring = [chr(crb) for crb in crab_positions if 31 < crb < 127]
secret_message = "".join(secret_decoder_ring)
secret_message
print(secret_decoder_ring)


# Inefficient approach
loop_pos = crab_positions.copy()
fuel = []
for apos in crab_positions:
    val_removed = loop_pos.copy()
    val_removed.remove(apos)
    fuel.append([abs(i - apos) for i in val_removed])

final_fuel_vals = []
# sum each list
final_fuel_vals.append([sum(i) for i in fuel])
min(final_fuel_vals[0])

"""part b
As it turns out, crab submarine engines don't burn fuel at a constant rate.
Instead, each change of 1 step in horizontal position costs 1 more unit of
fuel than the last: the first step costs 1, the second step costs 2, the
third step costs 3, and so on.
Make up your damn minds, crabbies
"""

# Inefficient approach
min_val, max_val = min(crab_positions), max(crab_positions)
loop_pos = crab_positions.copy()
final_fuel_tax = []
# Consider all vals in the range
for apos in range(min_val, max_val):
    print(apos)
    calc_fuel = [abs(i - apos) for i in loop_pos]
    # Add tax
    final_fuel_tax.append([sum(list(range(1, i + 1))) for i in calc_fuel])

final_fuel_vals_tax = []
# Sum each list to get final cost
final_fuel_vals_tax.append([sum(i) for i in final_fuel_tax])
min(final_fuel_vals_tax[0])


# get total fuel
# 1 to diff + 1
diff = 16 - 5
fuel_tax = list(range(1, diff + 1))
sum(fuel_tax)
