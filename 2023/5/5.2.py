def get(num, ranges):
    for range in ranges:
        c = num - range[1]
        if (0 <= c <= range[2]):
            return range[0] + c
    return(num)

def intersect(r1, r2):
    s1, e1 = r1[0], r1[0] + r1[1]
    s2, e2 = r2[0],  r2[0] + r2[2]
    if s1 > e2 or s2 > e1:
        return False
    else:
        l = (max(s1,s2), min(e1,e2))
    
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
def check(n):
    r = [(n, 1)]
    for i in range(7):
        for c in maps[6-i]:
            for rs in r:
                # print(r)
                r = intersect(rs, c)

(check(82))

# lo = 0
# hi = 10000
# while lo < hi:
#     mid = lo + (hi-lo)/2
#     if (check(mid)):
#         hi = mid
#     else:
#         lo = mid+1