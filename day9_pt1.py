import collections

f = open("input_day9.txt", "r")
# f = open("input_day9_pt1.txt", "r")

sequence = f.read().split("\n")

preamble = collections.deque()


def does_num_follow_rule(number):
    global preamble
    for i in range(0, len(preamble)):
        for j in range(i+1, len(preamble)):
            num1 = int(preamble[i])
            num2 = int(preamble[j])
            if num1 + num2 == number:
                return True
    return False


for i in range(0, len(sequence)):
    current_number = int(sequence[i])
    if i < 25:
        pass
    else:
        if not does_num_follow_rule(current_number):
            print(current_number)
            break
        preamble.popleft()
    preamble.append(current_number)
