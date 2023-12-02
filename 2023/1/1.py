pairs = [('one', 'o1e'), ('two', 't2'), ('three', 't3e'), ('four', '4'), ('five', '5e'), ('six', '6'), ('seven', '7n'), ('eight', 'e8t'), ('nine', 'n9e')]
s = 0
for line in open("1.in"):
    [(line := line.replace(w,d)) for w,d in pairs] #delete line for part 1
    l = [int(char) for char in line[0:-1] if ord(char) < 58 ]
    print(s := s + (l[0]*10 + l[-1]))

# print(sum := sum + (int(re.search(r'\d', line.rstrip()).group(0))*10 + int(re.search(r'\d', line.rstrip()[::-1]).group(0))))

#unreadable but 1 less line:
    # [(line := line.replace(w,d)) for w,d in pairs] #comment this line out for part 1
    # print(s := s + sum([10*int(k[0]) + int(k[-1]) for k in ["".join(filter(lambda x: ord(x)<58, line[0:-1]))]]))

#pt 1 one liner:
# print(sum([int(l[0] + l[-1]) for l in ["".join(filter(lambda x: x.isdigit(), line)) for line in open("1.in")]]))