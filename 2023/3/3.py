def notIn(t1, ls):
    for tup in ls:
        if(t1 == tup):
            return False
    return True

def add(ls, pos, prev, next):
    if(prev < pos < next):
        ls.append(pos)

dict = {

}
# LINE = 140
LINE = 140
# LINE = 10
visited = []
symbols = []
sum = 0
for row, line in enumerate(open("3/3.in")):
    num = ""
    for i, char in enumerate(line.rstrip()):
        position = row * LINE + i - 1
        prev = row * LINE - 1
        next = (row+1) * LINE
        # print(prev)
        # print(next)
        if 48 <= ord(char) <= 57:
            num += char
        else:
            length = len(num)
            if length > 0:
                # print("number: " + num)
                # print(position)
                indexes = []
                add(indexes, position - length, prev, next)
                add(indexes, position + 1, prev, next)
                for j in range(length+2):
                    add(indexes, (position - LINE - length) + j, (row-1) * LINE - 1, next)
                    add(indexes, (position + LINE - length) + j, prev, (row+2) * LINE)
                    # indexes.append((position - LINE - length) + j)
                    # indexes.append((position + LINE - length) + j)
                for index in indexes:
                    # print(index)
                    try:
                        dict[index].append((num, position))
                    except:
                        dict[index] = [(num, position)]

            if (char != '.'):
                symbols.append(position+1)
            num = ''
    length = len(num)
    if length > 0:
        position += 1
        # print("number: " + num)
        # print(num)
        # print(position)
        indexes = []
        add(indexes, position - length, prev, next)
        # add(indexes, position + 1, prev, next)
        for j in range(length+2):
            add(indexes, (position - LINE - length) + j, (row-1) * LINE - 1, next)
            add(indexes, (position + LINE - length) + j, prev, (row+2) * LINE)
            # indexes.append((position - LINE - length) + j)
            # indexes.append((position + LINE - length) + j)
        for index in indexes:
            print(index)
            try:
                dict[index].append((num, position))
            except:
                dict[index] = [(num, position)]
    

for symbol in symbols:
    # print(symbol)
    try:
        c = dict[symbol]
    except:
        continue
    if len(c) == 2:
        sum += int(c[0][0]) * int(c[1][0])
        # if(q not in visited):
            # print(symbol)
            # print(q[0])
            # sum += int(q[0])
            # visited.append(q)

# print(visited)
print(sum)
# print(len(dict.keys()))
# print(dict)
# print(symbols)


#9
#19
#29

#525479
#526498
#low