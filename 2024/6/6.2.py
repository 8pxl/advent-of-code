import a
board = []
pos = 0 + 0j
dir = -1j
i = 0
def checkLoop(pos, dir,y,x):
    vis = [(pos, dir)]
    while True:
        next = pos + dir
        if not ((0 <= next.real < len(board[0])) and (0 <= next.imag < len(board))):
            return False
        # print (x == int(next.real) and y == int(next.imag))
        while (board[int(next.imag)][int(next.real)] == '#') or ((x == int(next.real)) and (y == int(next.imag))):
            dir *= 1j 
            next = pos + dir
        pos = next
        if (pos, dir) not in vis:
            vis.append((pos, dir))
        else:
            return True
for line in open("6/6.in").readlines():
    if '^' in line:
        pos = complex(line.index('^'), i)
    board.append(list(line.rstrip()))
    i += 1
count = 0
for k in a.a:
    print(count)
    if (checkLoop(pos, dir, int(k.imag),int(k.real))):
        count += 1
print(count)