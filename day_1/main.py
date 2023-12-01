
total = 0

data = []

tmp_list = []

with open("day_1/input.txt") as f:
    data = f.readlines()

for line in data:
    for c in line:
        if c.isdigit():
            tmp_list.append(c)
    if len(tmp_list) > 1:
        string_val = "".join([tmp_list[0], tmp_list[-1]])
        total += int(string_val)
        tmp_list = []
    elif len(tmp_list) == 1:
        string_val = "".join([tmp_list[0], tmp_list[0]])
        total += int(string_val)
        tmp_list = []

print(total)
