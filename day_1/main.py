
total = 0

# data = []

data = [
    # "two1nine",
    # "eightwothree",
    # "abcone2threexyz",
    # "xtwone3four",
    # "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

valid_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


tmp_list = []

# with open("day_1/input.txt") as f:
#     data = f.readlines()

for line in data:
    tmp_string = line
    for key in valid_dict.keys():
        if key in tmp_string:
            print(key)
            index = tmp_string.find(key)
            output = tmp_string[:index] + valid_dict[key] + tmp_string[index:]
            tmp_string = output
    print(tmp_string)
    for c in tmp_string:
        if c.isdigit():
            tmp_list.append(c)
    print(tmp_list)
    if len(tmp_list) > 1:
        string_val = "".join([tmp_list[0], tmp_list[-1]])
        total += int(string_val)
        tmp_list = []
    elif len(tmp_list) == 1:
        string_val = "".join([tmp_list[0], tmp_list[0]])
        total += int(string_val)
        tmp_list = []

print(total)
