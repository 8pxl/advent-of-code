next = {
    'M':'S',
    'S': 'M',
    'X': '-1',
    'A': '-1'
}
count = 0
def check(ls, q):
    for i in range(2):
        if next[ls[q[i]]] != ls[q[i+2]]:
            return False
    return True
    
#2595 too high
with open("4/4.in") as f:
    ls = []
    width = 0
    for line in f.readlines():
        if width == 0:
            width = len(line.rstrip())
        for char in line.rstrip():
            ls.append(char)
    for i in range(1, width-1):
        for j in range(1, width-1):
            index = i * width +j
            if (ls[index] == 'A'):
                q = (index-width-1, index-width+1, index+width+1, index+width-1)
                if (check(ls, q)):
                    print(index)
                    count += 1
        
    print(count)