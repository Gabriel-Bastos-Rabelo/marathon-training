class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        position = [0] * (len(num1) + len(num2))
        p = len(position) -1
        num1 = num1[::-1]
        num2 = num2[::-1]

       

        for i in num1:
            index = p
            for k in num2:
                position[index] += int(i) * int(k)
                position[index-1] += position[index] //10
                position[index] = position[index] % 10
                index -= 1
            p -= 1
        i = 0
        while True:
            if i < len(position) and position[i] == 0:
                i += 1
            else:
                break
        
        if sum(position) == 0:
            return "0"
        return "".join(map(str, position[i:]))