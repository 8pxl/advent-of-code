import re
pairs = [('one', 'on1ne'), ('two', 'tw2wo'), ('three', 'thr3ree'), ('four', 'fo4ur'), ('five', 'fi5ve'), ('six', 'si6ix'), ('seven', 'se7ven'), ('eight', 'ei8ght'), ('nine', 'ni9ne')]
sum = 0;
for line in open("1.in"):
    _ = [0 for w,d in pairs if (line := line.replace(w,d))]
    print(sum := sum + (int(re.search(r'\d', line.rstrip()).group(0))*10 + int(re.search(r'\d', line.rstrip()[::-1]).group(0))))