
#leetcode 2375

res = []


def dfs(frase, current, index, n, letra):
    if len(current) == n+1:
        res.append(current.copy())
        return
    else:
        for i in range(1, 10):
            if i not in current:
                if index != 0 and letra == "I" and index < len(frase):
                    if i > current[len(current) - 1]:
                        current.append(i)
                        if frase[index] == "I":
                            dfs(frase, current, index+1, n, "I")
                        else:
                            dfs(frase, current, index+1, n, "J")

                        current.pop()
                elif index != 0 and letra == "J" and index < len(frase):

                    if i < current[len(current) - 1]:
                        current.append(i)
                        if frase[index] == "I":
                            dfs(frase, current, index+1, n, "I")
                        else:
                            dfs(frase, current, index+1, n, "J")

                        current.pop()

                elif index == 0:
                    current.append(i)
                    if frase[index] == "I":
                            dfs(frase, current, index+1, n, "I")
                    else:
                        dfs(frase, current, index+1, n, "J")

                    current.pop()
                elif letra == "I":
                    if i > current[len(current) - 1]:
                        current.append(i)
                        dfs(frase, current, index+1, n, "J")

                        current.pop()
                elif letra == "J":
                    if i < current[len(current) - 1]:
                        current.append(i)
                        dfs(frase, current, index+1, n, "J")

                        current.pop()


                
                

    return res


#solution 2

ans = ""
def fun(index, res_so_far, pattern):
    global ans
    if ans:
        return

    if index >= len(pattern):
        ans = ''.join(str(item) for item in res_so_far)
        return

    last_digit = res_so_far[-1]
    for i in range(1, 10):
        appended = False
        if pattern[index] == 'I' and i > last_digit and i not in res_so_far:
            appended = True
            res_so_far.append(i)
            fun(index+1, res_so_far, pattern)
        elif pattern[index] == 'D' and i < last_digit and i not in res_so_far:
            appended = True
            res_so_far.append(i)
            fun(index+1, res_so_far, pattern)

        if appended:
            res_so_far.pop(-1)

fun(0, [1], "IIIDIDDD")

print(ans)