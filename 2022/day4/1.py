inp = open("usaco/advent-of-code/2022/day4/input")
over = 0
for line in inp:
    fi = line.strip().split(',')
    p1 = list(map(int,fi[0].split('-')))
    p2 = list(map(int,fi[1].split('-')))
    #pray that keys remain unique...
    hash = {p1[0] : p1[1], p2[0] : p2[1]}
    if(hash[min(p1[0],p2[0])] >= hash[max(p1[0],p2[0])]):
        over += 1
print(over)
#somehow it worked!
