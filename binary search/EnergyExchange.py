#https://codeforces.com/contest/68/problem/B

def isPossible(value, lista, k):
    falta = 0
    excede = 0
    for i in lista:
        if i < value:
            falta += value - i
        else:
            excede += i - value

    return excede - (excede *k)/100 >= falta


def binarySearch(lista, k):
    l = 0
    r = max(lista)

    while(l <= r):
        mid = l + (r - l)/2
        if(isPossible(mid, lista, k)):
            l = mid + 0.000000001
        else:
            r = mid - 0.000000001

    return l


n, k = map(int, input().split())
lista = list(map(int, input().split()))

print(f'{binarySearch(lista, k):.9f}')