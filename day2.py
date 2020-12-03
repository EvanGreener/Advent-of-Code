f = open("input_day2.txt", "r")
passwords = f.read().split("\n")

valid_passowords = 0
policy = ""
password = ""
for i in range(0, len(passwords)):
    row = passwords[i].split(":")
    policy = row[0]
    password = row[1].replace(" ", "")
    first_position = ""
    second_position = ""
    letter = ""
    first_check_done = False
    second_check_done = False

    for c in range(0, len(policy)):
        if str.isnumeric(policy[c]) and not first_check_done and not second_check_done:
            first_position += policy[c]
            if not str.isnumeric(policy[c+1]):
                first_check_done = True
                continue

        if str.isnumeric(policy[c]) and first_check_done and not second_check_done:
            second_position += policy[c]
            if not str.isnumeric(policy[c+1]):
                second_check_done = True
                continue

        if str.isalpha(policy[c]) and first_check_done and second_check_done:
            letter = policy[c]
            continue

    print(
        f"1st pos = {first_position}, 2nd pos = {second_position}, letter = {letter}, password: \'{password}\'")

    occurences = 0
    if password[int(first_position) - 1] == letter:
        occurences += 1
    if password[int(second_position) - 1] == letter:
        occurences += 1

    if occurences == 1:
        valid_passowords += 1

print(f"# of valid passwords: {valid_passowords}")
