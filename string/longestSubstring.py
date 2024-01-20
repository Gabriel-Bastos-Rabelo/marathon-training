#3 leetcode

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        t = len(s)
        maior = 0
        for i in range(t):
            if s[i] in s[l: r]:
                while s[i] in s[l : r]:
                    l += 1
                r += 1

            else:
                r += 1
                maior = max(maior, r - l)

        return maior
     