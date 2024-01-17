n = int(input())

lista = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y'];
for i in range(n):

    s = input()
    t = len(s)
    

    l = 0
    r = t-1

    isPalindrome = True
    while(l < r):
        if (s[l] == s[r]) and (s[l] in lista and s[r] in lista):
            l += 1
            r -= 1

        else:
            isPalindrome = False
            break

    if(s[l] not in lista):
        isPalindrome = False

    if(isPalindrome):
        print("yes")
    else:
        print("no")
            

    