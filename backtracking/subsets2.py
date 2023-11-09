def dfs(nums, lista_geral, current, index):
    nums.sort()
    if current not in lista_geral:
        lista_geral.append(current.copy())
        print(current)

    if(index < len(nums)):
        current.append(nums[index])
        dfs(nums, lista_geral, current, index+1)
        current.pop()
        dfs(nums, lista_geral, current, index+1)



    


def backtracking(res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            backtracking(res,i+1,subset,nums)
            subset.pop()


res = []
backtracking(res, 0, [], [1, 4, 4])

print(res)


