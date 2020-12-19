f = open("input_day8.txt", "r")
instructions = f.read().split("\n")
accumulator = 0


def boot_code_terminates(new_op, new_line):
    global accumulator
    line = 0
    instructions_executed = set()
    while(line+1 != len(instructions) and line not in instructions_executed):
        instructions_executed.add(line)
        op, arg = instructions[line].split()
        previous_line = line
        if line == new_line:
            if new_op == "jmp":
                line += int(arg)
            else:
                line += 1
        elif op == "acc":
            accumulator += int(arg)
            line += 1
        elif op == "jmp":
            line += int(arg)
        else:
            line += 1

    return line + 1 == len(instructions)


for i in range(0, len(instructions)):
    op = instructions[i].split()[0]
    new_op = "acc"
    if op == "jmp":
        new_op = "nop"
    elif op == "nop":
        new_op = "nop"

    if boot_code_terminates(new_op, i):
        break
    accumulator = 0

print(f"Value of acc = {accumulator}")
