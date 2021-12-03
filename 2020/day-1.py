import os

data_path = "data-1.txt"
path = os.path.join(os.getcwd(), "2020", data_path)

with open(path) as f:
    lines = f.readlines()

final_vals = [int(anum.strip()) for anum in lines]
"""Find the two numbers that add up to 2020 and multiply them"""

for anum in final_vals:
    for anum2 in final_vals[1:]:
        if anum + anum2 == 2020:
            print("DONESEYS", anum, anum2)
            a = anum
            b = anum2

print("Answer part a is: ", a*b)

""" Find 3 numbers that add to 2020 and multiply"""

for anum in final_vals:
    for anum2 in final_vals[1:]:
        for anum3 in final_vals[2:]:
            if anum + anum2 + anum3 == 2020:
                print("DONESEYS", anum, anum2, anum3)
                a = anum
                b = anum2
                c = anum3

answer = a*b*c
print("The answer is: ", answer)
