pairs = [('one', 'o1e'), ('two', 't2'), ('three', 't3e'), ('four', '4'), ('five', '5e'), ('six', '6'), ('seven', '7n'), ('eight', 'e8t'), ('nine', 'n9e')]
s = 0
for line in open("1.in"):
    [(line := line.replace(w,d)) for w,d in pairs] #delete line for part 1
    l = [int(char) for char in line[0:-1] if ord(char) < 58 ]
    print(s := s + (l[0]*10 + l[-1]))