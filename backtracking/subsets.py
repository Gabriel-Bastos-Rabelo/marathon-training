# subsets 78 leetcode

ans = []
def backtracking(start, end, current_list, nums):
    ans.append(current_list.copy())

    for i in range(start, end):
        current_list.append(nums[i])
        backtracking(i+1, end, current_list, nums)
        current_list.pop()
        