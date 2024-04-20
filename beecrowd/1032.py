import sys
sys.setrecursionlimit(100000)
def ehPrimo(k):
    if k % 2 == 0:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
        
    return True



def proximoPrimo(k):
    res = k + 1 if k % 2 == 0 else k + 2
    while True:
        if ehPrimo(res):
            return res
        
        res += 2



def josephus(n, k):
    i = 1
    ans = 0

    while i <= n:
        ans = (ans + k) % i
        print(ans)
        k = proximoPrimo(k)
        i += 1


    return ans + 1


def Josh(person, k, index):
   
    # Base case , when only one person is left
    if len(person) == 1:
        print(person[0])
        return 
        

    # find the index of first person which will die
    index = ((index+(k - 1))%len(person))

    # remove the first person which is going to be killed
    person.pop(index)

    k = proximoPrimo(k)

    # recursive call for n-1 persons
    Josh(person,k,index)



while True:
    n = int(input())
    if n == 0:
        break
    people = [i for i in range(1, n + 1)]
    Josh(people, 2, 0)

