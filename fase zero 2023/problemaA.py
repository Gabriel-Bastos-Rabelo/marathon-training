s = input()

dicionario = {}
dicionario['O'] = 0
dicionario['X'] = 0
for i in s:
    if i == 'X':
        
        dicionario['X'] += 1
    else:
        
        dicionario['O'] += 1


if dicionario['O'] > 1 or dicionario['X'] >= 3:
    print("?")

elif s[0] == s[2]:
    print("*")
else:
    print("Alice")