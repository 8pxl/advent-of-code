f = open("1.in")
count, index = 0, 50
for line in f.readlines():
    num = (1 if line[0] == "R"  else -1) * int(line[1:])
    index = (index + num) % 100
    if index == 0:
        count+=1
print(count)
