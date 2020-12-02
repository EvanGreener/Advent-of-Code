f = open("input.txt", "r")
inputs = f.read().split("\n")
inputs.pop()

inputs_length = len(inputs)
num1 = -1
num2 = -1
num3 = -1
for i in range(inputs_length):
    num1 = int(inputs[i])
    for j in range(i, inputs_length):
        num2 = int(inputs[j])
        for k in range(j, inputs_length):
            num3 = int(inputs[k])
            if(num1 + num2 + num3 == 2020):
                print(
                    f"{num1} + {num2} + {num3} = 2020\nAnswer: {num1 * num2 * num3}")
