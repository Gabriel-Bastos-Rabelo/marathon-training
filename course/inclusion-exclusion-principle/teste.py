continuo = True
zeroDepoisDeUm = False
binario = "00001"

for index, l in enumerate(binario):
        if l == '1':
            if zeroDepoisDeUm:
                continuo = False
                break

        else:
            if index >=1 and binario[index - 1] == '1':
                zeroDepoisDeUm = True

print(continuo)