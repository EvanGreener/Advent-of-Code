import re

f = open("input_day4.txt", "r")
passports = f.read().split("\n\n")
valid_passports = 0


def check_fields(fields):
    for field in fields:
        key = field.split(":")[0].replace(" ", "")
        value = field.split(":")[1].replace(" ", "")
        if key == "byr" and not (1920 <= int(value) <= 2002):
            return False
        elif key == "iyr" and not (2010 <= int(value) <= 2020):
            return False
        elif key == "eyr" and not (2020 <= int(value) <= 2030):
            return False
        elif key == "hgt":
            if re.match("^[0-9]{3}cm$", value):
                height = value.replace("cm", "")
                if not (150 <= int(height) <= 193):
                    return False
            elif re.match("^[0-9]{2}in$", value):
                height = value.replace("in", "")
                if not (59 <= int(height) <= 76):
                    return False
            else:
                return False
        elif key == "hcl" and not(re.match("^#[0-9a-f]{6}", value)):
            return False
        elif key == "ecl":
            if not(re.match("(amb|blu|brn|gry|grn|hzl|oth){1}", value)):
                return False
        elif key == "pid" and not (re.match("[0-9]{9}", value)):
            return False
    return True


fields_correct = False
for i in range(0, len(passports)):
    passport = passports[i]
    fields = passport.split()
    num_fields = len(fields)
    if num_fields == 7:
        if "cid" not in passport:
            fields_correct = check_fields(fields)
            if fields_correct:
                valid_passports += 1
            print(f"{i+1}.) {fields_correct}")
    elif num_fields == 8:
        fields_correct = check_fields(fields)
        if fields_correct:
            valid_passports += 1
        print(f"{i+1}.) {fields_correct}")


print(f"Valid passports = {valid_passports}, len(passports): {i+1}")
