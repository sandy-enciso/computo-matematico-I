# Objetivo: Implemente una función que ordene ascendentemente una lista. 
# La función ordena es programa que recibe como argumento una lista y regresa otra lista ordenada.


def elimina(lista, elemento):
    l = []
    eliminado = False
    for i in lista:
        if i == elemento and not eliminado:
            eliminado = True
        else:
            l = l + [i]
    return l

def maximo(lista):
    elemento = lista[0]
    for i in lista:
        if i > elemento:
            elemento = i
    return elemento

def ordena(lista):
    resultado = []
    lista_aux = lista
    for _ in lista:
        max_elem = maximo(lista_aux)
        resultado = [max_elem] + resultado
        lista_aux = elimina(lista_aux, max_elem)
    return resultado


print(ordena([7,4,10,2,1])) # -> [1,2,4,6,10]
print(ordena([7,1,4,2,3,2,1])) # -> [1,1,2,2,3,4,7]