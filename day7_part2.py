f = open("input_day7.txt", "r")
# f = open("input_day7_pt1.txt", "r")
# f = open("input_day7_pt2.txt", "r")
rules = f.read().split("\n")

color_rules = dict()
for rule in rules:
    color, definition = rule.split(" bags contain ")
    definition = definition.replace(".", "").split(", ")
    color_rules[color] = definition

# 1 + (1 * (3 + (3 * 0) + 4 + (4 * 0))) + 2 + ( 2 * (5 + (5 *0) + 6 + (6*0)))

# 0 + 1 + 1 * (3 )


def num_bags(color):
    bag_count = 0
    definition = color_rules[color]
    if definition[0] == "no other bags":
        return 0
    else:
        for bag in definition:
            number = int(bag[0:2])
            if "bags" in bag:
                bag = bag.replace(" bags", "")[2:]
            else:
                bag = bag.replace(" bag", "")[2:]

            bag_count += number
            bag_count += number * num_bags(bag)
    return bag_count


print(num_bags("shiny gold"))
