input = open("1.in")
pairs = [ ('one', 'on1ne'), ('two', 'tw2wo'), ('three', 'thr3ree'), ('four', 'fo4ur'), ('five', 'fi5ve'), ('six', 'si6ix'), ('seven', 'se7ven'), ('eight', 'ei8ght'), ('nine', 'ni9ne')]
sum = 0;
for line in input:
    _ = [0 for w,d in pairs if (line := line.replace(w,d))]
    l = [int(char) for char in line.rstrip() if ord(char) < 58]
    print(sum := sum + (l[0]*10 + l[-1]))