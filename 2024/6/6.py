board = []
pos = 0 + 0j
dir = -1j
i = 0
for line in open("6/6.in").readlines():
    if '^' in line:
        pos = complex(line.index('^'), i)
    board.append(list(line.rstrip()))
    i += 1
vis = [pos]
while True:
    next = pos + dir
    if not ((0 <= next.real < len(board[0])) and (0 <= next.imag < len(board))):
        break
    while board[int(next.imag)][int(next.real)] == '#':
        dir *= 1j 
        next = pos + dir
    pos = next
    if pos not in vis:
        vis.append(pos)
    print(pos)
print(vis)
print(len(vis))
#4710 low