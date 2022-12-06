inp = open("usaco/advent-of-code/2022/day3/input")

priority = 0   
lines = [''.join(set(line.strip())) for line in inp.readlines()]
triples = [lines[i:i+3] for i in range(0,len(lines),3)]
for triple in triples:
    for char in triple[0]:
        if char in triple[1] and char in triple[2]:
            uni = ord(char)
            if uni <= 90:
                uni -= 38
            else:
                uni -= 96
            priority += uni
print(priority) 