f = open("1.in")
count = 0
index = 50
for line in f.readlines():
    print("------------")
    sign = 1 if line[0] == "R"  else -1

    t = 100 if sign > 0 else 0
    if index == 0:
        dist = 100
    else:
        dist = t - (sign * index)
    old = index

    num = sign * int(line[1:])
    raw = index+num
    index = raw % 100
    print(num, dist)
    if (abs(num) >= dist):
        count += 1 + ((abs(num)-dist) // 100)
        print("adding ", (1 if (old!=0) else 0) + ((abs(num)-dist) // 100))
    print(index, line.rstrip())
print(count)

input_file = "1.in"
