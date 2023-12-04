total = 0
for line in open("4/4.in"):
    l = line.split()[2:]
    c = [list(map(int, l[:10])), list(map(int, l[10+1:]))]
    num = len([1 for num in c[1] if num in c[0]]) - 1
    if (num>=0):
        print(total := total + (1 << num))