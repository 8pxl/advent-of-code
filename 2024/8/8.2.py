map, dim, pts = {}, [], set()
for i, line in enumerate(open("8/8.in")):
    dim = [len(line.rstrip()), i+1]
    for j, char in enumerate(line.rstrip()):
        if char != '.':
            map.setdefault(char, []).append(complex(j, i))
for node in map.keys():
    for k in map[node]:
        for other in map[node]:
            if k == other:
                continue
            mult = 1
            while True:
                cand = k - (mult * (other - k))
                if (0 <= cand.real < dim[0]) and (0 <= cand.imag < dim[1]):
                    pts.add(cand)
                else:
                    if (mult < 0): break
                    mult = 0
                mult += 1 if mult > 0 else -1
print(len(pts))