inp = open("usaco/advent-of-code/2022/day3/input")

priority = 0
for line in inp:
    mid = int(len(line.strip())/2)
    first = ''.join(set((line[:mid])))
    last = ''.join(set((line[mid:])))
    for char in first:
        if char in last:
            uni = ord(char)
            if uni <= 90:
                uni -= 38
            else:
                uni -= 96
            priority += uni
print(priority)