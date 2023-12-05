import math
def get(num, ranges):
    for range in ranges:
        c = num - range[1]
        if (0 <= c <= range[2]):
            return range[0] + c
    return(num) 
f = open("5/5.in")
seeds = tuple(map(int,f.readline().split()[1:]))
maps = []
for i in range(7):
    maps.append([])
i = -1
for line in f:
    line = line.rstrip()
    if (line == ""):
        continue
    if(line[-1] == ':'):
        i += 1
        continue
    maps[i].append(tuple(map(int,line.split())))
low = math.inf
for seed in seeds:
    num = seed
    for i in range(7):
        num = get(num, maps[i])
    low = min(low, num)
print(low)