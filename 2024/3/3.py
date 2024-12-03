import re
sum = 0
with open("3/3.in") as f:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", f.read())
    for match in matches:
        match = match[4:].split(",")
        # print(int(match[0]) , int(match[1][:-1]))
        sum += int(match[0]) * int(match[1][:-1])
print(sum)