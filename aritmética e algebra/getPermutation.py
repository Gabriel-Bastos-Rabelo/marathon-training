def getPermutation(n, k):
        nums = [i for i in range(1, n+1)]
        k -= 1
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        res=[]
        for i in range(n):
            index = int(k / factorial[n - 1 - i])
            res.append(str(nums[index]))
            nums.remove(nums[index])
            k = k % factorial[n - 1 - i]
        return ''.join(res)



print(getPermutation(4, 9))