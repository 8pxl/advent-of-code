total = 0
for line in open("4/4.in"):
    l = line.split()[2:]
    num = len([1 for num in l[11:] if num in l[:10]]) - 1
    if (num>=0):
        print(total := total + (1 << num))