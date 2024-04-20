linha = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"


while True:
    try:

        s = input()

        nova_palavra = ""

        for i in s:
            if i == " ":
                nova_palavra += " "
                continue
            if i in linha:
                index = linha.index(i)
                nova_palavra += linha[index-1]
        

        print(nova_palavra)
    except EOFError:
        break
