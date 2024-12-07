def check(num, const):
    print(num, const)
    if (len(const) == 1): return num == const[0]
    if (num % const[-1] == 0):
        if check(num // const[-1], const[:-1]):
            return True
    l2 = len(str(const[-1]))
    l1 = len(str(num))
    if (l1 > l2 and num >= 0):
        if (int(str(num)[l1-l2:]) == const[-1]):
            if check(int(str(num)[:-l2]), const[:-1]):
                return True
    return check(num - const[-1], const[:-1])
sum = 0
for line in open("7/7.in"):
    line = line.split()
    num = int(line[0][:-1])
    if (check(num, tuple(map(int, line[1:])))):
        sum += num
print(sum)