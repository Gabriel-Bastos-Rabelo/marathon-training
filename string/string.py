#Find the First and Last Occurrence of a Character in the String:

str = "Learn Competitive Programming with GFG!"
first = str.find('m')
last = str.rfind('m')
if first != -1:
    print(f"First Occurrence of m is at index = {first}")
if last != -1:
    print(f"Last Occurrence of m is at index = {last}")




#reverse a string
str = "Learn Competitive Programming with GFG!"
print(f"Reverse = {str[::-1]}")

print()


# Append a character/string at the end of the String:

str = "Learn Competitive Programming with "
str = "".join([str, "GFG!"])
print(f"New String = {str}")
print()


#Sorting a string:
str = "Learn Competitive Programming with GFG!"
str = "".join(sorted(str))
print(f"Sorted string = {str}")


#Substring extraction:
Str = "Learn Competitive Programming with GFG!"
print(f"Substring from index 6 to 16 = {Str[6:17]}")


#check if starts with
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)









