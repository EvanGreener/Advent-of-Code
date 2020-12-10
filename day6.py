f = open("input_day6.txt", "r")
groups = f.read().split("\n\n")
yes_count = 0

for group_as in groups:
    yes_qs = set({"a", "b", "c", "d", "e", "f", "g", "h",
                  "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                  "s", "t", "u", "v", "w", "x", "y", "z"})
    for person_as in group_as.split("\n"):
        yes_qs_2 = set()
        for c in person_as:
            if (str.isalpha(c)):
                yes_qs_2.add(c)
        yes_qs = yes_qs.intersection(yes_qs_2)
    yes_count += len(yes_qs)


print(f"sum = {yes_count}")
