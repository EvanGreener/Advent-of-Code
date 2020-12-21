# f = open("input_day10_sample copy.txt", "r")
f = open("input_day10.txt", "r")
joltages = f.read().split("\n")

for i in range(0, len(joltages)):
    joltages[i] = int(joltages[i])

joltages.sort()
joltages.insert(0, 0)

one_jolt_diffs = 0
# two_jolt_diffs = 0
three_jolt_diffs = 0
# other_diffs= 0
highest = set()
string_of_1s = 0
for i in range(1, len(joltages)):
    if joltages[i] - joltages[i-1] == 1:
        one_jolt_diffs += 1
        string_of_1s += 1
        highest.add(string_of_1s)
    # elif joltages[i] - joltages[i-1] == 2:
    #     two_jolt_diffs +=      1
    elif joltages[i] - joltages[i-1] == 3:
        three_jolt_diffs += 1
        string_of_1s = 0
    # else:
    #     other_diffs += 1

print(f"1 differnces = {one_jolt_diffs}")
# print(f"2 differences = {two_jolt_diffs}")
print(f"3 differences = {three_jolt_diffs}")
# print(f"other differences = {other_diffs}")
print(f"Highest number = {joltages[-1]}")
print(f"Length of sequence = {len(joltages)-1}")
print(f"longest string of 1s {highest}")
# Part 2

longest_string_of_1s = 0

# moves = len(joltages)
# target = joltages[-1]
# combinations = []
# current_combo = []
# for i in range(0, moves-1):
#     current_combo.append(0)

# print(f"Joltages: {joltages}")
# # print("1) Retrieving all combinations...")


# def add_all_combinations(move_num, total_moves, current_combo):
#     global combinations
#     if move_num == total_moves:
#         # print(f"\n{current_combo}\n")
#         combinations.append(current_combo.copy())
#     else:
#         for i2 in range(0, 4):
#             current_combo[move_num] = i2
#             add_all_combinations(
#                 move_num+1, total_moves, current_combo)


# add_all_combinations(0, moves-1, current_combo)

# # print("DONE!!")
# # print("2) Removing 0s...")

# combinations_no_0s = []
# for combo in combinations:
#     combinations_no_0s.append(list(filter((0).__ne__, combo)))
# combinations_no_0s.pop(0)
# # print(combinations_no_0s)

# # print("DONE!!")
# # print("3) Removing duplicates...")
# # print(f"length of list {len(combinations_no_0s)}")

# no_duplicates = set(tuple(i) for i in combinations_no_0s)

# # print(no_duplicates)

# # print("DONE!!")
# # print("4) Keeping only the configurations which add up to the highest number...")

# no_duplicates = list(no_duplicates)
# equals_target = []
# for i in range(0, len(no_duplicates)):
#     sum = 0
#     for j in range(0, len(no_duplicates[i])):
#         sum += no_duplicates[i][j]
#     if sum == target:
#         equals_target.append(no_duplicates[i])

# # print(f"Target = {target}")
# # print(equals_target)
# # print("DONE!!")
# # print("5) Finding number of valid configurations...")

# valid_configurations = []
# for i in range(0, len(equals_target)):
#     counter = 0
#     is_valid = True
#     for j in range(0, len(equals_target[i])):
#         counter += equals_target[i][j]
#         if counter not in joltages:
#             is_valid = False
#             break
#     if is_valid:
#         valid_configurations.append(equals_target[i])

# # print(valid_configurations)
# print(f"Number of valid configurations = {len(valid_configurations)}")

# 0 + 1 = 1 (0 * 2 + 1)
# 1 + 1 = 2 (1 * 2 - 0)
# 2 + 2 = 4 (2 * 2 - 0)
# 4 + 3 = 7 (4 * 2 - 1)
# 7 + 6 = 13 (7 * 2 - 1)
# 13 + 11 = 24 (13 * 2 - 2)
# 24 + 20 = 44 (24 * 2 - 4)
# 44 + 37 = 81 (44 * 2 - 7)
# 81 + 68 = 149 (81 * 2 - 13)
# 149 + 125 = 274 (149 * 2 - 24)
# 274 + 230 = 504 (274 * 2 - 44)
# 504 + 423 = 927 (504 * 2 - 81)

# one_jolt_diffs = 0
# two_jolt_diffs = 0
# three_jolt_diffs = 0
# for i in range(1, len(joltages)):
#     if joltages[i] - joltages[i-1] == 1:
#         one_jolt_diffs += 1
# for i in range(1, len(joltages)):
#     if joltages[i] - joltages[i-1] == 2 or joltages[i] - joltages[i-2] == 2:
#         two_jolt_diffs += 1
# for i in range(1, len(joltages)):
#     if joltages[i] - joltages[i-1] == 3 or joltages[i] - joltages[i-2] == 3 or joltages[i] - joltages[i-3] == 3:
#         three_jolt_diffs += 1

one_choice = 0
two_choices = 0
three_choices = 0
for i in range(0, len(joltages)-1):
    num_choices = 0
    for k in range(1, 4):
        if joltages[i] + k in joltages:
            num_choices += 1
    if num_choices == 1:
        one_choice += 1
    elif num_choices == 2:
        two_choices += 1
    else:
        three_choices += 1

# print(f"1 choice = {one_choice}")
# print(f"2 choices = {two_choices}")
# print(f"3 choices = {three_choices}")


# print(f"Length = {len(joltages)-1}")
# print(f"1 differnces = {one_jolt_diffs}")
# print(f"2 differences = {two_jolt_diffs}")
# print(f"3 differences = {three_jolt_diffs}")

one_1s = 0
two_1s = 0
three_1s = 0
four_1s = 0

current_1s = 0
for i in range(1, len(joltages)):
    if joltages[i] - joltages[i-1] == 1:
        current_1s += 1
    else:
        if current_1s == 1:
            one_1s += 1
        elif current_1s == 2:
            two_1s += 1
        elif current_1s == 3:
            three_1s += 1
        elif current_1s == 4:
            four_1s += 1
            
        current_1s = 0

print(
    f"Valid arrangements = {pow(1,one_1s) * pow(2, two_1s) * pow(4,three_1s) * pow(7,four_1s)}")
