k = list(open("9/9.in").read())
spaces = [int(k[i]) for i in range(len(k)) if i % 2 != 0]
spaces.append(0)
nums = [int(k[i]) for i in range(len(k)) if i % 2 == 0]
x = []
for i in range(len(nums)):
    x.extend([i] * nums[i])
    x.extend([-1] * spaces[i])
i = 0
print(x)
while i < len(x):
    if x[i] == -1:
        while (x[-1]) == -1:
            x.pop()
        x[i] = x.pop()
    i += 1
    # print(x)
#7593380618455 too high
print(sum([i * x[i] for i in range(len(x))]))