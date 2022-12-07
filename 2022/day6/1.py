inp = open("usaco/advent-of-code/2022/day6/input")
signal = inp.readline()
count = 0
for i in range(len(signal)-13):
    check = signal[i:i+14]
    for j in range(len(check)):
        if (check[j] in (check[:j] + check[j+1:])):
            count = 0
            break
        else:
            count += 1
    if(count == 14):
        print(i+14)
        break