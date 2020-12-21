# f = open("input_day11_sample.txt", "r")
f = open("input_day11.txt", "r")
rows = f.read().split("\n")

# 99 x 97 area

# Convert array of strings into 2d array of characters

seats = []
for i in range(0, len(rows)):
    row = []
    for c in rows[i]:
        row.append(c)
    seats.append(row)


for i in range(0, len(seats)):
    seats[i].insert(0, '.')
    seats[i].append('.')

top = []
for k in range(0, len(seats[0])):
    top.append('.')

bottom = []
for k in range(0, len(seats[0])):
    bottom.append('.')

seats.insert(0, top)
seats.append(bottom)


def apply_seating_rules():
    global seats
    seats_occupied = list()
    seats_empty = list()
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[0])):
            array = list()
            array.append(i)
            array.append(j)
            # 1st rule
            if seats[i][j] == "L":
                surrounding = str()
                surrounding += seats[i-1][j-1]
                surrounding += seats[i-1][j]
                surrounding += seats[i-1][j+1]

                surrounding += seats[i][j-1]
                surrounding += seats[i][j+1]

                surrounding += seats[i+1][j-1]
                surrounding += seats[i+1][j]
                surrounding += seats[i+1][j+1]

                if str(surrounding).count("#") == 0:
                    seats_occupied.append(array)
            #2nd rule
            elif seats[i][j] == "#":
                surrounding = str()
                surrounding += seats[i-1][j-1]
                surrounding += seats[i-1][j]
                surrounding += seats[i-1][j+1]

                surrounding += seats[i][j-1]
                surrounding += seats[i][j+1]

                surrounding += seats[i+1][j-1]
                surrounding += seats[i+1][j]
                surrounding += seats[i+1][j+1]

                if str(surrounding).count("#") >= 4:
                    seats_empty.append(array)

    for seat in seats_occupied:
        i, j = seat
        seats[i][j] = "#"

    for seat in seats_empty:
        i, j = seat
        seats[i][j] = "L"

    return [not seats_occupied, not seats_empty]


# occupied_empty, empty_empty = apply_seating_rules()
# occupied_empty, empty_empty = apply_seating_rules()
# occupied_empty, empty_empty = apply_seating_rules()
# occupied_empty, empty_empty = apply_seating_rules()
# occupied_empty, empty_empty = apply_seating_rules()
# occupied_empty, empty_empty = apply_seating_rules()
# for row in seats:
#     print(row)
# print(occupied_empty, empty_empty)

# Apply rules until state stays constant
while True:
    occupied_empty, empty_empty = apply_seating_rules()
    print(occupied_empty, empty_empty)
    if occupied_empty and empty_empty:
        break

# Count number of occupied seats
occupied_seats = 0
for i in range(0, len(seats)):
    for j in range(0, len(seats[0])):
        if seats[i][j] == "#":
            occupied_seats += 1
print(f"Number of occupied seats = {occupied_seats}")
