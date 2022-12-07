inp = open("usaco/advent-of-code/2022/day5/input")
containers = [[], [], [], [], [], [], [], [], []]
for i in range(8):
    curr = inp.readline()
    k = 0
    for j in range(0,27,3):
        c = (curr[k+j:j+k+3])[1].strip()
        if c:
            containers[k].insert(0,c)
        k+=1
inp.readline()
inp.readline()
for i in range(502):
    curr = inp.readline()
    com = curr.split()
    com = [int(com[1]), int(com[3])-1, int(com[5])-1]
    init = len(containers[com[2]])
    for i in range(com[0]):
        containers[com[2]].insert(init,containers[com[1]].pop())
for i in range(len(containers)):
    print(containers[i][-1], end = '')

