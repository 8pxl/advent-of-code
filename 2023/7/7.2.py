import functools

arr = []
cards = 'J23456789TQKA'
for line in open("7/7.in"):
    a,b = line.split()
    arr.append((a, int(b)))
# print(arr)
def strength(card):
    power = []
    repeat = {}
    for char in card[0]:
        if (char in repeat.keys()):
            repeat[char] += 1
        else:
            repeat[char] = 1
        power.append(cards.find(char))
    high = 0
    try:
        j = repeat.pop('J')
    except:
        j = 0
        pass
    temp = sorted(repeat.values())
    print(j)
    print(temp)
    #01 45
    first = temp[-1] + j
    try:
        second = temp[-2]
    except:
        second = 0
    if first >= 4:
        high = first + 2
    elif first >= 3:
        high = first + second
    elif first >= 2:
        high = first + second-1
    else:
        high = 1
    return(high, power)


print(strength(("QWWJJ", 0)))
def cmp(item1, item2):
    f1, f2 = strength(item1), strength(item2)
    if f1[0] > f2[0]:
        return 1
    elif f1[0] < f2[0]:
        return -1
    else:
        for i in range(5):
            if f1[1][i] > f2[1][i]:
                return 1
            elif f1[1][i] < f2[1][i]:
                return -1
    return True

# arr.sort(key=functools.cmp_to_key(cmp))

# print(arr)
ans = 0
for i in range(len(arr)):
    ans += ((i+1) * arr[i][1])
    # print((i+1), arr[i])
# print(arr)
# for k in arr:
#     k = strength(k)
#     print(k[0], [cards[z] for z in k[1]])
# print(ans)

# for i, k in enumerate(cmp1.c1.keys()):
#     if(k != arr[i][0]):
#         print(k, arr[i][0])

#253423074
#253423074
#247764477
#247577426

#253638586
#253638586