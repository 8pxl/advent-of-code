map = {}
dim = [0,0]
board = []
for i, line in enumerate(open("8/8.in")):
    dim[0] = len(line.rstrip())
    dim[1] = i+1
    board.append(list(line.rstrip()))
    for j, char in enumerate(line.rstrip()):
        if char != '.':
            if char not in map.keys():
                map[char] = [complex(j, i)]
            else:
                map[char].append(complex(j, i))
pts = set()
print(dim)
print(map)
for node in map.keys():
    for k in map[node]:
        for other in map[node]:
            if k == other:
                continue
            mult = 1
            while True:
                cand = k - (mult * (other - k))
                if (0 <= cand.real < dim[0]) and (0 <= cand.imag < dim[1]):
                    # if (board[int(cand.imag)][int(cand.real)] == '.'):
                    pts.add(cand)
                else:
                    if (mult < 0):
                        break
                    mult = 0
                mult+= 1 if mult > 0 else -1
for i in range(len(board)):
    for j in range(len(board[i])):
        if(complex(j, i) in pts):
            print('#', end = '')
        else:
            print(board[i][j], end = '')
    print()
print(pts)
print(len(pts))