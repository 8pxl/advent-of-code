#pt.1
inp = open("input")

mvs = {
    "A" : 3,
    "B" : 2,
    "C" : 1,
    "X" : 3, 
    "Y" : 2, 
    "Z" : 1
}

swap = {
    1 : 2,
    2 : 0,
    0 : 1,
    -1 : 0,
    -2 : 2
}

score = 0
for line in inp:
    curr = list(line.split())
    m1 = mvs[curr[0]]
    m2 = mvs[curr[1]]
    if m2 > m1:
        m1 += 3
    result = swap[(m1 - m2)]
    score += result * 3 + (4 - m2)

print(score)

#pt.2 (why is it so diff oml)

inp = open("input")