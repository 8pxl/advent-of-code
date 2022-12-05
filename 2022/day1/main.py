input = open("input")

highest = [0,0,0]
temp = 0

for line in input:
    if(not line == "\n"):
        n = int(line.replace("\n",""))
        temp += n

    else:
        for i in range(3):
            if temp > highest[i]:
                highest.pop()
                highest.insert(i,temp)
                break
        print(highest)
        temp = 0
print(sum(highest))