inp = open("usaco/advent-of-code/2022/day4/input")
count = 0
for line in inp:
    fi = line.strip().split(',')
    p1 = list(map(int,fi[0].split('-')))
    p2 = list(map(int,fi[1].split('-')))
    #pray that keys remain unique...
    hash = {p1[0] : p1[1], p2[0] : p2[1]}
    low = min(p1[0],p2[0])
    high = max(p1[0],p2[0])
    if(low <= hash[high] and hash[low] >= high):
        count += 1
print(count)
#somehow it worked!
    