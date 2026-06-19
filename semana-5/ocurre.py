# Contar las veces que ocurra un elemento dentro de una lista

def ocurre(lista, elemento):
    ocurrencias = 0
    for i in lista:
        if i == elemento:
            ocurrencias += 1
    return ocurrencias

print(ocurre([1,2,3,4,3,5,3], 3))