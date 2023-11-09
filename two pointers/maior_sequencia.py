def check(a, n, string, k):
    ret = 0
    r = 0
    cnt = 0
    for l in range(n):

        while (r < n and (cnt < k or string[r] != a)):

            if string[r] == a:
                cnt += 1

            r += 1

        # if string[l] == a:
        #     cnt -= 1

        if ret < r - l:
            ret = r - l

    return ret


resultado = check("a", 4, "baab", 1)
print(resultado)
