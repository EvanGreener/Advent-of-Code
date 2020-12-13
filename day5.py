f = open("input_day5.txt", "r")
seats = f.read().split("\n")
my_seat_id = 0


def get_row_id(string):
    binary = ""
    for c in string:
        if c == "F":
            binary += "0"
        else:
            binary += "1"
    return int(binary, 2)


def get_col_id(string):
    binary = ""
    for c in string:
        if c == "L":
            binary += "0"
        else:
            binary += "1"
    return int(binary, 2)


seat_ids = set()
for seat in seats:
    row_string, col_string = seat[0:7], seat[7:10]
    row_id = get_row_id(row_string)
    col_id = get_col_id(col_string)
    seat_id = row_id * 8 + col_id
    seat_ids.add(seat_id)

# print(seat_ids)
is_first_iteration = True
for seat in seat_ids:
    if is_first_iteration:
        is_first_iteration = False
    elif int(seat+1) not in seat_ids:
        print(seat+1)
        break
    elif int(seat-1) not in seat_ids:
        print(seat-1)
        break
