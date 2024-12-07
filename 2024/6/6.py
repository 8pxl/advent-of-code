board, pos, dir = [], 0+0j, -1j
for i, line in enumerate(open("6/6.in")):
    if '^' in line: pos = complex(line.index('^'), i)
    board.append(line.rstrip())
vis = {pos}
while 0 <= (next := pos + dir).real < len(board[0]) and 0 <= next.imag < len(board):
    while board[int(next.imag)][int(next.real)] == '#':
        dir *= 1j
        next = pos + dir
    vis.add(pos := next)
print(len(vis))