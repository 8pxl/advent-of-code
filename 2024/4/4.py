next = {
    'X':'M',
    'M': 'A',
    'A': 'S',
}
count = 0
daddy = 0
visited = []
def bfs(ls, i, width, depth, dir):
    global count
    q = (i-1, i+1, i-width, i+width, i-width-1, i-width+1, i+width-1, i+width+1)
    if dir == -1:
        adj = q
    else:
        adj = [q[dir]]
    if ls[i] == 'S':
        if depth == 3:
            pair = (daddy, i)
            if pair not in visited:
                visited.append(pair)
                count += 1
        return
    print(i, adj)
    for j,a in enumerate(adj):
        if a >= 0 and a < len(ls) and (abs(a % width - i%width) <= 1):
            print(ls[i])
            if ls[a] == next[ls[i]]:
                bfs(ls, a, width, depth + 1, j if dir == -1 else dir)
#2595 too high
with open("4/4.in") as f:
    ls = []
    width = 0
    for line in f.readlines():
        if width == 0:
            width = len(line.rstrip())
        for char in line.rstrip():
            ls.append(char)
    for i in range(len(ls)):
        if (ls[i] == 'X'):
            daddy = i
            bfs(ls, i, width, 0, -1)
    print(count)
    # print(visited)