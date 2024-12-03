import re
sum = 0
with open("3/3.in") as f:
    matches = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", f.read())
    do = True
    for match in matches:
        if (match == "do()"): do = True
        elif (match == "don't()"): do = False
        else:
            if do:
                match = match[4:].split(",")
                sum += int(match[0]) * int(match[1][:-1])
print(sum)