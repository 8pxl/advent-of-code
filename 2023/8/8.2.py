f = open('8/8.in')
step = f.readline().rstrip()
step = [1 if char == 'R' else 0 for char in step]
print(step)
adj = {}
starts = []
for line in f:
    l = line.split()
    if(l[0][-1]) == "A":
        starts.append(l[0])
    adj[l[0]] = (l[2][1:4], l[3][0:3])
arr = []
for start in starts:
    curr = start
    visited = []
    count = 0
    while True:
        # print(curr)
        curr = adj[curr][step[count % len(step)]]
        if((curr, (count % len(step))) in visited):
            # print(visited)
            break
        visited.append((curr, count % len(step)))
        if(curr[-1] == 'Z'):
            arr.append(count)
        count += 1

def lcm(arr):
    import math
    from functools import reduce
    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

# print(starts)
# print(arr)
arr = [k+1 for k in arr]
print(lcm(arr))