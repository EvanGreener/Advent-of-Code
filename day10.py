f = open("input_day10_sample.txt", "r")
# f = open("input_day10.txt", "r")
joltages = f.read().split("\n")

for i in range(0, len(joltages)):
    joltages[i] = int(joltages[i])

joltages.sort()
joltages.insert(0, 0)


three_jolt_diffs = 0
one_jolt_diffs = 0
for i in range(1, len(joltages)):
    if joltages[i] - joltages[i-1] == 1:
        one_jolt_diffs += 1
    elif joltages[i] - joltages[i-1] == 3:
        three_jolt_diffs += 1
    else:
        pass

# print(three_jolt_diffs * one_jolt_diffs)


# Part 2

def to_base4(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 4)
        nums.append(str(r))
    return ''.join(reversed(nums))


# 1) Number of moves must be less than length of list - 1
# 2) the number of all joltages must add up to the final number
# 3) Difference between joltages <= 3

# 0,1,3,4
# moves = 3
# target_joltage = 4
# 0 + 0 + 0     0
# 0 + 0 + 1     1
# 0 + 0 + 2     2
# 0 + 0 + 3     3
# 1 + 0 + 0     1
# 1 + 0 + 1     2
# 1 + 0 + 2     3
# 1 + 0 + 3     4
# 1 + 1 + 0     2
# 1 + 1 + 1     3
# 1 + 1 + 2     4
# 1 + 1 + 3     5
# 1 + 2 + 0     3
# 1 + 2 + 1     4
# 1 + 2 + 2     5
# 1 + 2 + 3     6
# 1 + 3 + 0     4
# 1 + 3 + 1     5
# 1 + 3 + 2     6
# 1 + 3 + 3     7

combinations = list()
moves = len(joltages)
target = joltages[-1]

current_combo = []
for i in range(0, moves-1):
    current_combo.append(0)


# for i in range(0, moves-1):
#     for i2 in range(0, 4):
#         current_combo[i] = i2
#         for j in range(i+1, moves-1):
#             for j2 in range(0, 4):
#                 current_combo[j] = j2
#                 for k in range(j+1, moves-1):
#                     for k2 in range(0, 4):
#                         current_combo[k] = k2
#                         print(current_combo)


def add_all_combinations(move_num, total_moves, current_combo):
    if move_num == total_moves:
        print(current_combo)
    else:
        for i2 in range(0, 4):
            current_combo[move_num] = i2
            add_all_combinations(move_num+1, total_moves, current_combo)


add_all_combinations(0, moves-1, current_combo)
