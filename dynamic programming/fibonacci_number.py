#leetcode 509
memo = {}
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    elif n in memo:
        return memo[n]
    
    memo[n]  = fibonacci(n-1) + fibonacci(n-2)

    

    return memo[n]


print(fibonacci(5))




