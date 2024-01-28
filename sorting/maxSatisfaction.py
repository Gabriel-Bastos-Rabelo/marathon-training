def maxSatisfaction(self, satisfaction: List[int]) -> int:
        t = len(satisfaction)
        dp = [0] * t

        satisfaction.sort()

        for i in range(t):
            soma = 0
            time = 1
            for j in range(i, t):
                soma += (time * satisfaction[j])
                time += 1

            if i != 0:
                dp[i] = max(dp[i-1], soma)
            else:
                dp[i] = max(soma, 0)

        return dp[t-1]