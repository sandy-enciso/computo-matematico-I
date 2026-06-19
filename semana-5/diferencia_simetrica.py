# objetivo: Calcular la diferencia simétrica entre dos conjuntos

def diferencia_simetrica(lista1, lista2):
    l = []

    for i in lista1:
        if i not in lista2:
            l = l + [i]

    for i in lista2:
        if i not in lista1:
            l = l + [i]

    return l


print(diferencia_simetrica([3,2,1,4], [5,6,3,4]))  # [2,1,5,6]