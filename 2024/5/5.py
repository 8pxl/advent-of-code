with open("5/5.in") as f:
    dict = {}
    sum = 0
    def check(line):
        bad = []
        for num in line:
            if num in bad:
                return False
            if num in dict:
                bad.extend(dict[num])
        return True
    for l in f.readlines():
        if(len(l) == 1): continue
        if ('|' in l): 
            l = tuple(map(int, l.rstrip().split('|')))
            if l[1] not in dict:
                dict[l[1]] = [l[0]]
            else:
                dict[l[1]].append(l[0])
        else: 
            l = tuple(map(int, l.rstrip().split(',')))
            if check(l): sum += l[len(l)//2]
    print(sum)