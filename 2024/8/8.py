map, dim, pts = {}, [], set()
for i, line in enumerate(open("8/8.in")):
    dim = [len(line.rstrip()), i+1]
    for j, char in enumerate(line.rstrip()):
        if char != '.':
            map.setdefault(char, []).append(complex(j, i))
for node in map.keys():
    for k in map[node]:
        for other in map[node]:
            if k == other: continue
            cand = k - (other - k)
            if (0 <= cand.real < dim[0]) and (0 <= cand.imag < dim[1]):
                pts.add(cand)
print(len(pts))