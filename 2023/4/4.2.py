cards = [0] * 206
for i,line in enumerate(open("4/4.in")):
    cards[i] += 1
    l = line.split()[2:]
    for j in range(i+1, i + 1 + len([1 for num in l[11:] if num in l[:10]])):
        cards[j] += (1 * cards[i])
print(sum(cards))