def isPalindrome(sol):
    return sol[0] == sol[0][::-1]


def dfs(index, curr, s, res):
    if (index == len(s)):

        
        res.append(curr.copy())
        return
    else:
        for i in range(index, len(s)):
            

            if isPalindrome(sol):
                dfs(i+1, curr + sol, s, res)

    return res


print(dfs(0, [], "aaab", []))


