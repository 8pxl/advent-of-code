f = open("2/2.in")
count = 0


def strictly_increasing(L):
    return all(L[i] < L[i+1] for i in range(len(L)-1))


def strictly_decreasing(L):
    return all(L[i] > L[i+1] for i in range(len(L)-1))


def monotonic(L):
    return strictly_increasing(L) or strictly_decreasing(L)


for line in f.readlines():
    nums = tuple(map(int, line.split()))
    q = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    n = [1 <= abs(num) <= 3 for num in q]
    count += (n.count(n[0]) == len(n) and monotonic(nums))
print(count)