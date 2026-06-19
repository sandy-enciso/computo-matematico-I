# Diferencia entre dos conjuntos.

def diferencia_conjuntos(lista1, lista2):
    l = []
    for i in lista1:
        if i not in lista2:
            l = l+[i]
    return l

print(diferencia_conjuntos([1, 2, 3], [2, 3, 4]))