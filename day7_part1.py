f = open("input_day7.txt", "r")
# f = open("day7_example.txt", "r")
rules = f.read().split("\n")
shiny_gold_bag_count = 0

color_rules = dict()
for rule in rules:
    color, definition = rule.split(" bags contain ")
    definition = definition.replace(".", "").split(", ")
    color_rules[color] = definition

colors_with_gold = set()
colors_without_gold = set()


def contains_gold(color, i):
    colors_at_each_level.insert(i, color)
    definition = color_rules[color]
    if definition[0] == "no other bags":
        colors_with_gold.union(colors_at_each_level)
        return False
    elif color in colors_with_gold:
        return True
    elif color in colors_without_gold:
        return False
    else:
        i += 1
        for bag in definition:
            if "bags" in bag:
                bag = bag.replace(" bags", "")[2:]
            else:
                bag = bag.replace(" bag", "")[2:]

            colors_at_each_level.insert(i, bag)

            if "shiny gold" in bag:
                colors_with_gold.union(colors_at_each_level)
                return True
            else:
                has_gold = False
                if "bags" in bag:
                    has_gold = contains_gold(bag, i + 1)
                else:
                    has_gold = contains_gold(bag, i + 1)

                if has_gold:
                    return has_gold
        return False


for color in color_rules:
    colors_at_each_level = list()
    if contains_gold(color, 0):
        # add_colors_in_set(color, True)
        shiny_gold_bag_count += 1
        print(f"{shiny_gold_bag_count}: {color}")
    else:
        # add_colors_in_set(color, False)
        print(f"X {color}")


print(f"Shiny gold bag count = {shiny_gold_bag_count}")


# def add_colors_in_set(color, with_gold):
#     definition = color_rules[color]
#     if definition[0] == "no other bags":
#         return
#     if with_gold:
#         colors_with_gold.add(color)
#     else:
#         colors_without_gold.add(color)

#     for bag in definition:
#         if "bags" in bag:
#             add_colors_in_set(
#                 bag.replace(" bags", "")[2:], with_gold)
#         else:
#             add_colors_in_set(
#                 bag.replace(" bag", "")[2:], with_gold)
