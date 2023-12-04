cards = [0] * 206
for i,line in enumerate(open("4/4.in")):
    cards[i] += 1
    l = line.split()[2:]
    c = [list(map(int, l[:10])), list(map(int, l[11:]))]
    for j in range(i+1, i + 1 + len([1 for num in c[1] if num in c[0]])):
        cards[j] += (1 * cards[i])
print(sum(cards))