mrgb = [12, 13, 14]
sum = 0
for line in open("2/2.in"):
    # print(line)
    l = line.split()
    game = int(l[1][:-1])
    # print(game)
    l = l[2:]   
    print(l)
    rgb = [0,0,0]
    type = -1
    num = 0
    last = False
    for i,k in enumerate(l):
        if(last):
            rgb = [0,0,0]
        last = k == l[-1]   
        if i%2 == 0:
            num = int(k)
        else:
            if("red" in k):
                rgb[0] += num
            if("green" in k):
                rgb[1] += num
            if("blue" in k):
                rgb[2] += num
            if((k[-1] == ';') or last):
                for i in range(3):
                    # print("rgb: " + str(rgb[i]))
                    if(rgb[i] > mrgb[i]):
                        break
                else:
                    if(last):
                        sum += game
                    last = True
                    continue
                break


print(sum)
