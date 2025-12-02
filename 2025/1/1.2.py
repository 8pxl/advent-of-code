f = open("1.in")
count, index = 0, 50
for line in f.readlines():
    sign = 1 if line[0] == "R" else -1
    #get distance until next 0
    t = 100 if sign > 0 else 0
    dist = 100 if index == 0 else t - (sign * index)
    old = index
    #if the step size is greater than the distance to the next 0, then we can increment our count
    step = sign * int(line[1:])
    index = (index + step) % 100
    if (abs(step) >=dist):
        count += 1 + ((abs(step)-dist) // 100)
print(count)
