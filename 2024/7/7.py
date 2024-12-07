def check(num, const):
    print(num, const)
    if (len(const) == 1):
        if (num == const[0]):
            return True
        else:
            return False
    if (num % const[-1] == 0):
        if check(num / const[-1], const[:-1]):
            return True
    return check(num - const[-1], const[:-1])
sum = 0
for line in open("7/7.in"):
    line = line.split()
    num = int(line[0][:-1])
    if (check(num, tuple(map(int, line[1:])))):
        sum += num
print(sum)