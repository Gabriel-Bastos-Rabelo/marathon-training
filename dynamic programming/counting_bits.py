
#leetcode 338, não entendi

def couting_bits(n):
    memo = [0] * n+1


    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        memo[i] = i + memo[i - offset]