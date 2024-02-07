m, n = 3, 7

memo = [[0] * n for i in range(m)]

def backtracking(point, memo):
    if point[0] >= m or point[1] >= n:
        return 0
    if point[0] == m - 1 and point[1] == n-1:
        memo[point[0]][point[1]] += 1
        return 1
    if memo[point[0]][point[1]] != 0:
        return memo[point[0]][point[1]]

    else:
        right = backtracking((point[0], point[1] + 1), memo)
        left = backtracking((point[0] + 1, point[1]), memo)
        memo[point[0]][point[1]] = (right + left)

        return memo[point[0]][point[1]]

print(m, n)
backtracking((0,0), memo)
print(memo[0][0])