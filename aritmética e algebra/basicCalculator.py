class Solution:
   
    def calculate(self, s: str) -> int:

        def update(sign, num):
            if sign == "+":
                stack.append(num)
            else:
                stack.append(-num)

        i = 0
        num = 0
        sign = "+"
        stack = []
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+-":
                update(sign, num)
                num = 0
                sign = s[i]

            elif s[i] == "(":
                num, index = self.calculate(s[i + 1:])
                i += index

            elif s[i] == ")":
                update(sign, num)
             
                return sum(stack), i + 1

            i += 1

        update(sign, num)
        return sum(stack)
