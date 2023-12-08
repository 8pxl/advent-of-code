f = open('8/8.in')
step = f.readline().rstrip()
step = [1 if char == 'R' else 0 for char in step]
print(step)
adj = {}
for line in f:
    l = line.split()
    adj[l[0]] = (l[2][1:4], l[3][0:3])
curr = "AAA"
count = 0
while curr != "ZZZ":
    curr = adj[curr][step[count % len(step)]]
    print(curr)
    count += 1
print(count)


