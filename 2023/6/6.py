f = open("6/6.in")
times = list(map(int,f.readline().split()[1:]))
distances = list(map(int,f.readline().split()[1:]))
def calcDist(atime, time):
    return((time-atime) * atime)
count = [0,0,0,0]
for i in range(4):
    for j in range(1, times[i]):
        if(calcDist(j, times[i]) > distances[i]):
            count[i] = count[i]+1
            
total = 1
for c in count:
    print(c)
    total *= c
print(total)
