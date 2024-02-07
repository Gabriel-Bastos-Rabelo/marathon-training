def countDigitOne(n):
    i = 1
    res = 0
    while i <= n:
        prefix = int(n/(i*10))
        digit = int((n/i) % 10)
        suffix = int(n % i)

        if (digit == 0):
            res += prefix * i
        elif (digit == 1):
            res += prefix*i + suffix + 1
        else:
            res += (prefix + 1)*i

        i *= 10

    return res


countDigitOne(13)


