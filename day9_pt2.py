import collections

f = open("input_day9.txt", "r")
# f = open("input_day9_pt1.txt", "r")
sequence = f.read().split("\n")

target = 25918798

current_sum = 0
summands = []
for i in range(0, len(sequence)):
    current_sum = int(sequence[i])
    summands.append(int(sequence[i]))
    summands = []
    for j in range(i+1, len(sequence)):
        current_sum += int(sequence[j])
        summands.append(int(sequence[j]))
        if current_sum == target:
            summands.sort()
            print(summands[0] + summands[-1])
        elif current_sum > target:
            break
        else:
            pass
