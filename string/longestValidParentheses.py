
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for index, i in enumerate(s):
            if i == "(":
                stack.append(index)

            else:
                if len(stack) > 0 and s[stack[len(stack) - 1]] == "(":
                    stack.pop(len(stack) - 1)
                else:
                    stack.append(index)

        a = len(s)
        b = 0
        longest = 0
        while(len(stack) != 0):
            b = stack.pop(len(stack) - 1)
            longest = max(longest, a-b-1)
            a = b
        
        longest = max(longest, a)

        return longest