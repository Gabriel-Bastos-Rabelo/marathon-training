#We need total numbers not greater than a given number ‘N‘ and divisible by first 3 prime numbers={2,3,5}.

#brute force

count = 0
n = 100
numbers = [2,3,5]
def isDivisible(n, numbers):
    for i in numbers:
        if n % i == 0:
            return True
        
    return False
            
for i in range(n):
    count += 1 if isDivisible(i, numbers) else 0

print(count)


# using inclusion exclusion principle

#∣A∪B∪C∣=∣A∣+∣B∣+∣C∣−∣A∩B∣−∣B∩C∣−∣A∩C∣+∣A∩B∩C∣

count = n//2 + n//3 + n//5 - n//(2 * 3) - n//(2 * 5) - n//(3 * 5) + n//(2 * 3 * 5)
print(count)

