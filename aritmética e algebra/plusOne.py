class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def somarUm(lista, indice):
            if indice == 0:
                if lista[indice] + 1 > 9:
                    lista[indice] = 0
                    lista.insert(0, 1)
                    return
                else:
                    lista[indice] += 1
                    return
            else:
                if lista[indice] + 1 > 9:
                    lista[indice] = 0
                    somarUm(lista, indice - 1)
                    return
                else:
                    lista[indice] += 1
                    return 

        somarUm(digits, len(digits) - 1)
        return digits
