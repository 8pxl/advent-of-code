f = open("1/1.in")
l = []
r = []
for line in f.readlines():
    temp = tuple(map(int, line.split()))
    l.append(temp[0])
    r.append(temp[1])
l = sorted(l)
r = sorted(r)
sum  = 0
for i in range(len(l)):
    sum += l[i] * len([0 for j, x in enumerate(r) if x == l[i]])
print(sum)