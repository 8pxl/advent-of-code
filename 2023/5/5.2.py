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
    tup = tuple(map(int,line.split()))
    maps[i].append(tup)
print(maps)