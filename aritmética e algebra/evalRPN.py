class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lista = ["+", "-", "/", "*"]
        for i in tokens:
            if i not in lista:
                stack.append(int(i))

            else:
                if i == "+":
                    res = stack[len(stack) - 2] + stack[len(stack) - 1]
                    stack.pop()
                    stack[len(stack) - 1] = res
                elif i == "-":
                    res = stack[len(stack) - 2] - stack[len(stack) - 1]
                    stack.pop()
                    stack[len(stack) - 1] = res
                elif i == "*":
                    res = stack[len(stack) - 2] * stack[len(stack) - 1]
                    stack.pop()
                    stack[len(stack) - 1] = res

                else:

                    res = int(stack[len(stack) - 2] / stack[len(stack) - 1])
                    stack.pop()
                    stack[len(stack) - 1] = res

                

        return stack[0]