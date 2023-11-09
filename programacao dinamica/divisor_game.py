def divisorGame(n, jogador):
    if n == 2:
        if jogador == "Alice":
            return True
        else:
            return False
    else:
        for i in range(1, n):
            result = False
            if n % i == 0:
                if jogador == "Alice":
                    result = divisorGame(n-i, "João")
                else:
                    result = divisorGame(n-i, "Alice")
                
                if result == True:
                    return True
    return False


print(divisorGame(2, "Alice"))