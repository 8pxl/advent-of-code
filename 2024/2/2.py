def check(nums):
    diff = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    monotonic = (all(x > 0 for x in diff) or all(x < 0 for x in diff))
    return all([1 <= abs(num) <= 3 for num in diff]) and monotonic

p1, p2 = 0, 0
with open("2/2.in") as f:
    for line in f.readlines():
        nums = tuple(map(int, line.split()))
        p1 += check(nums)
        p2 += sum([check(nums[:i] + nums[i+1:]) for i in range(len(nums))]) > 0
print(p1, p2)