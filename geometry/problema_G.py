p = input()

nova = ""
for i in range(len(p)):
    if i % 2 == 0:
        nova += p[i].capitalize()

    else:
        nova += p[i]

print(nova)
