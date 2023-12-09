total = 0
for line in open('9/9.in'):
    arr = [list(map(int, line.split()))]
    curr = 0
    while any(arr[-1]):
        arr.append([arr[curr][i+1] - arr[curr][i] for i in range(0, len(arr[curr])-1)])
        curr += 1
    diff = 0
    for i in range(len(arr)-1, -1, -1):
        diff = arr[i][-1] + diff
    print(total := total+diff)