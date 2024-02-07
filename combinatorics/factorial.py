#Question 1. A class has just 3 seats vacant. Three people P, A, and R arrive at the same time. In how many ways can P, A, and R be arranged on those 3 vacant seats?
def fatorial(n):
    res = 1

    for i in range(1, n+1):
        res *= i

    return res

fatorial(3)

#Question 2. Find the number of ways of arranging 5 people if 2 of them always sit together?
fatorial(4)

#Question 3. Find all the three-letter words beginning and ending with a vowel. Given that repetition of alphabets is not allowed.
fatorial(7*6*24)

    