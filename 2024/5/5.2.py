import time
import functools
start_time = time.time()
dict = {}
sum = 0

def cmp(x, y):
    if x not in dict:
        return 0
    if y in dict[x]:
        return 1
    return 0
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return 1
        elif less_than(y, x):
            return -1
        else:
            return 0
    return compare

def check(line):
    bad = []
    for num in line:
        if num in bad:
            return False
        if num in dict:
            bad.extend(dict[num])
    return True
for l in open("5/5.in").readlines():
    if(len(l) == 1): continue
    if ('|' in l): 
        l = tuple(map(int, l.rstrip().split('|')))
        if l[1] not in dict:
            dict[l[1]] = [l[0]]
        else:
            dict[l[1]].append(l[0])
    else: 
        l = list(map(int, l.rstrip().split(',')))
        if not check(l): 
            l = sorted(l, key=functools.cmp_to_key(make_comparator(cmp)))
            sum += l[len(l)//2]
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
