def countOrders(self, n: int) -> int:    
    def backtracking(n):
        if n == 1:
            return 1
        else:
            return n * (n * 2 - 1) * backtracking(n - 1)


    return backtracking(n)%((10 ** 9) + 7)


