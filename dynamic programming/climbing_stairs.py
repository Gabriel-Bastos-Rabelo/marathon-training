#Solução recursiva, backtracking, não passa no tempo limite
#maneiras de subir uma escada com N degraus, podendo subir 1 ou 2 degraus por vez
ans = 0
memo = {}
def climbingStairs(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        if n in memo:
            return memo[n]
        else:
            soma = climbingStairs(n-1) + climbingStairs(n-2)

            memo[n] = soma

            return soma
    


print(climbingStairs(5))


