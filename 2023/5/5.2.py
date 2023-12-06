import time
start_time = time.time()
def get(num, ranges):
    for range in ranges:
        c = num - range[0]
        if (0 <= c <= range[2]):
            return range[1] + c
    return(num)
    
def check(n, seeds):
    num = n
    for i in range(7):
            num = get(num, maps[6-i])
    for i in range(int(len(seeds) / 2)):
        if (seeds[2*i] <= num <= seeds[2*i] + seeds[2*i + 1]):
            return True
    return False

f = open("5/5.in")
seeds = tuple(map(int,f.readline().split()[1:]))
maps = [[] for _ in range(7)]
i = -1
for line in f:
    line = line.rstrip()
    if (line == ""):
        continue
    if(line[-1] == ':'):
        i += 1
        continue
    maps[i].append(tuple(map(int,line.split())))
lo = 0
hi = 1000000000
# print(i)
while lo < hi:
    mid = int(lo + (hi-lo)/2)
    if (check(mid, seeds)):
        hi = mid
    else:
        lo = mid+1
print("--- %s seconds ---" % (time.time() - start_time))
print(mid)  