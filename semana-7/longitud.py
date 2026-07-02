# Longitud. Contar el numero de elementos que tiene una lista

def longitud(lista):
    len = 0
    while lista != []:
        len += 1
        lista = lista[1:]
    return len


print(longitud([1,2,3,4,5]))