# Objetivo: Toma los n primeros elementos de una lista

def toma(lista, n):
    l = []
    contador = 0
    for i in lista:
        if contador < n:
            l = l + [i]
        contador+=1
    return l


print(toma([1,2,3,4,5,6,7,8], 5))