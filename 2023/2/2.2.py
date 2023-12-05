sum = 0
for line in open("2/2.in"):
    l = line.split()
    game = int(l[1][:-1])
    l = l[2:]
    num = 0
    rgb = [0,0,0]
    prgb = [0,0,0]
    for i, item in enumerate(l):
        if (i%2 == 0):
            num = int(item)
        else:
            if("red" in item):
                rgb[0] += num
            if("green" in item):
                rgb[1] += num
            if("blue" in item):
                rgb[2] += num

            if(item[-1] == ';' or i == len(l)-1):
                for i in range(3):
                    prgb[i] = max(prgb[i], rgb[i])
                rgb = [0,0,0]
    power = 1
    for i in range(3):
        power *= prgb[i]
    sum += power
print(sum)