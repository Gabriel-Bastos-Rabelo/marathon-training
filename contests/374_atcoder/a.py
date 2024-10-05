s =  input()


t = len(s)

if t < 3:
    print("No")

else:
    p = s[t-3:t]

    if p == 'san':
        print("Yes")

    else:
        print("No")
