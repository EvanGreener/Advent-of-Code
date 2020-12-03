f = open("input_day3.txt", "r")
map = f.read().split("\n")
trees_encountered = 0
# trees_already_encountered = set()


def num_trees(x_step, y_step):
    num_trees = 0
    # global trees_already_encountered
    x = 0
    for y in range(y_step, len(map), y_step):
        row = map[y]
        x += x_step
        if (x > len(row) - 1):
            x -= len(row)

        if(row[x] == "#"):
            # trees_already_encountered.add((x, y))
            num_trees += 1
    print(num_trees)
    return num_trees


trees = num_trees(1, 1) * num_trees(3, 1) * num_trees(5, 1) * \
    num_trees(7, 1)*num_trees(1, 2)
print(trees)
