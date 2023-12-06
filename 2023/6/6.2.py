f = open("6/6.in")
time = int(''.join(f.readline().split()[1:]))
distance = int(''.join(f.readline().split()[1:]))

def calcDist(atime, time):
    return((time-atime) * atime)

lo = 0
hi = time-1
while lo < hi:
    mid = int(lo + (hi-lo)/2)
    # print(calcDist(mid, time))
    if (calcDist(mid, time) > distance):
        hi = mid
    else:
        lo = mid+1

first = mid

lo = 1
hi = time-1
while lo < hi:
    mid = int(lo + (hi-lo+1)/2)
    if (calcDist(mid, time) > distance):
        lo = mid
    else:
        hi = mid - 1

second = mid
print(second-first)

#34788143
#34788144