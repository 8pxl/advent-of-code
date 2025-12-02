ranges = [
    list(map(int, x.split("-"))) 
    for x in open("2.in").readline().split(",")
]
ans = 0
for r in ranges:
    rstr = tuple(map(str, r))
    lengths = list(map(len, rstr))
    if (lengths[0]%2 != 0):
        r[0] = (10 ** lengths[0])
        lengths[0] += 1
    if (lengths[1]%2 != 0):
        lengths[1] -= 1
        r[1] = (10 ** lengths[1]) - 1
    rstr = tuple(map(str, r))
    for l in range(lengths[0], lengths[1]+1, 2):
        l2 = l//2
        if (l == lengths[0]):
            qmin = int(rstr[0][:l2])
            if int(rstr[0][l2:]) > qmin:
                qmin += 1
        else:
            qmin = 10 ** (l2-1)

        if (l == lengths[1]):
            qmax = int(rstr[1][:l2])
            if int(rstr[1][l2:]) < qmax:
                qmax -= 1
        else:
            qmax = (10 ** (l2))-1
        if qmin <=qmax:
            for v in range(qmin, qmax+1):
                ans += int(str(v) * 2)
print(ans)
