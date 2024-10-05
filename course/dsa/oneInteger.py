def solve(nums):
    left = 0
    right = len(nums) - 1
    res = 0
    nums.sort()

    while right - left > 0:
        num1 = nums[left]
        num2 = nums[left + 1]
        res += num1 + num2
        left += 2
        nums.append(num1 + num2)
        right += 1
        nums.sort()


    return res


print(solve([1,2,3]))
