f = open("2/2.in")
count = 0


def strictly_increasing(L):
    return all(L[i] < L[i+1] for i in range(len(L)-1))


def strictly_decreasing(L):
    return all(L[i] > L[i+1] for i in range(len(L)-1))


def monotonic(L):
    return strictly_increasing(L) or strictly_decreasing(L)

def check(nums):
    q = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    n = [1 <= abs(num) <= 3 for num in q]
    return ((n.count(True) == len(n)) and monotonic(nums))

for line in f.readlines():
    nums = tuple(map(int, line.split()))
    safe = check(nums)
    # print(safe)
    if not safe:
        for i in range(len(nums)):
            if (not safe):
                print(f"num to check: {(nums[:i] + nums[i+1:])}")
                print(f"value: {check(nums[:i] + nums[i+1:])}")
                safe = check(nums[:i] + nums[i+1:])
            else:
                # print(line.rstrip() + " " + str(safe))
                break
    count += safe
print(count)