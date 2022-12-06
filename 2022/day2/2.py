inp = open("input")

oc = {
    "X" : 1, 
    "Y" : 0, 
    "Z" : 2
}

mvs = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
}

scores = 0
for line in inp:
    curr = list(line.split())
    m1 = mvs[curr[0]]
    m2 = oc[curr[1]]
    move = (m1 + (2-m2)) % 3 + 1
    if m2 < 2:
        m2 = int(not m2)
    scores += (move + (m2 * 3))

print(scores)