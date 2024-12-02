adj = [[] for i in range(19600)]
arr = []
width = 0
for line in open("10/10.in"):
    for c in line.rstrip():
        arr.append(c)
print(arr)