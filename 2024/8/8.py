map = {}
dim = [0,0]
for i, line in enumerate(open("8/8.in")):
    dim[0] = len(line.rstrip())
    dim[1] = i+1
    for j, char in enumerate(line.rstrip()):
        if char != '.':
            if char not in map.keys():
                map[char] = [complex(j, i)]
            else:
                map[char].append(complex(j, i))
pts = set()
for node in map.keys():
    for k in map[node]:
        for other in map[node]:
            if k == other:
                continue
            cand = k - (other - k)
            if (0 <= cand.real < dim[0]) and (0 <= cand.imag < dim[1]):
                pts.add(cand)
print(len(pts))