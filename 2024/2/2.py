count = 0
with open("2/2.in") as f:
    for line in f.readlines():
        nums = tuple(map(int, line.split()))
        diff = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        n = [1 <= abs(num) <= 3 for num in diff]
        monotonic = (all(x > 0 for x in diff) or all(x < 0 for x in diff))
        count += (n.count(True) == len(n) and monotonic)
print(count)