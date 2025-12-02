ranges = [
    list(map(int, x.split("-"))) 
    for x in open("2.in").readline().split(",")
]
ans = 0
for r in ranges:
    rstr = tuple(map(str, r))
    lengths = list(map(len, rstr))
    for i in range(r[0], r[1]+1):
        stri = str(i)
        length= len(stri)
        for j in range(1, (length//2) +1):
            if (length//j) * stri[:j] == stri:
                ans += i
                break
print(ans)
