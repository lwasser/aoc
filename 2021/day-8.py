import os

# data_path = "day-8-test.txt"
data_path = "day-8-data.txt"
path = os.path.join(os.getcwd(), "2021", "data", data_path)
with open(path) as f:
    all_data = [line.strip().split(" ") for line in f.readlines()]

unique_counts = [2, 3, 4, 7]
unique_nums = []
for line in all_data:
    # Count digits in second part
    # Count items with 2, 4, 7, 8 chars
    unique_nums.extend(
        [len(val) for val in line[11:15] if len(val) in unique_counts]
    )

# ANSWER 539
print("The number of 1,4,7,8 is:", len(unique_nums))

"""Part B"""


def get_key(adict, achar, sort_str=False):
    if sort_str:
        achar = "".join(sorted(achar))
        return list(adict.keys())[list(adict.values()).index(achar)]
    else:
        return list(adict.keys())[list(adict.values()).index(achar)]


def join_number(alist_nums):
    return int("".join([str(i) for i in alist_nums]))


example = [
    "acedgfb",
    "cdfbe",
    "gcdfa",
    "fbcad",
    "dab",
    "cefabd",
    "cdfgeb",
    "eafb",
    "cagedb",
    "ab",
    "",
    "cdfeb",
    "fcadb",
    "cdfeb",
    "cdbaf",
]

# Map unique values value to number of unique chars
# chars that make up number: number value
val_count = {2: 1, 4: 4, 3: 7, 7: 8}


def calculate_overlap(str1, str2):
    return len(list(set(str1) & set(str2)))


# TODO: in theory i don't have to remove the sorted values each time to reduce
# some code. this code is fragile and would need lots of extra checks
all_final_nums = []
for i, a_line in enumerate(all_data):
    code_lookup = {}
    sorted_codes = a_line[0:10]
    # Sort by length then alphabetical
    sorted_codes.sort(key=len)
    # Alphabetical
    sorted_codes = ["".join(sorted(acode)) for acode in sorted_codes]

    # Get unique and add to dict
    unique_codes = [
        astr for astr in sorted_codes if len(astr) in unique_counts
    ]
    # Loop through and Id known values 1,4,7,8
    for acode in unique_codes:
        code_lookup[val_count[len(acode)]] = acode
        sorted_codes.remove(acode)

    # Now infer based upon patterns - all codes have 5 or 6 chars left now
    # Handle 5's first just cause - would be more robust with a length check
    # Id test for this before proceeding in a more robust workflow
    # If its 5 digits its 2,3 or 5
    for acode5 in sorted_codes[0:3]:
        overlap1 = calculate_overlap(acode5, code_lookup[1])
        # if overlap is 2 it's a 3
        if overlap1 == 2:
            code_lookup[3] = acode5
            sorted_codes.remove(acode5)
        # It's either 2 or 5 if overlap is not 2
        # Compare it to 4 to distinguish last 2
        else:
            overlap4 = calculate_overlap(acode5, code_lookup[4])
            # It's a 5 if overlap is 3
            if overlap4 == 3:
                code_lookup[5] = acode5
                sorted_codes.remove(acode5)
            # what's left is 2
            else:
                code_lookup[2] = acode5
                sorted_codes.remove(acode5)
        # Should have 3 codes left to process
        # 0, 6, 9 left
        for acode6 in sorted_codes:
            overlap1 = calculate_overlap(acode6, code_lookup[1])
            # if overlap is 1 it's a 6
            if overlap1 == 1:
                code_lookup[6] = acode6
            # It's a 9 if overlap with 4 is 4 else it's a 0
            else:
                overlap4 = calculate_overlap(acode6, code_lookup[4])
                if overlap4 == 4:
                    code_lookup[9] = acode6
                else:
                    code_lookup[0] = acode6
    # Now create final numbers
    # alphabetize them all
    final_codes = [
        "".join(sorted(a_final_line)) for a_final_line in a_line[11:15]
    ]
    final_nums = []
    for a_final_code in final_codes:
        final_nums.append(get_key(code_lookup, a_final_code))
    # combine finals
    all_final_nums.append(join_number(final_nums))

# Answer 1084606
print("The final sum is", sum(all_final_nums))
