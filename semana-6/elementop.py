# Objetivo: Implemente la función elementoP que regresa el elemento e de una posición pos dada. 
# La función recibe dos argumentos: la lista y la posición pos. La función regresa el elemento e de dicha posición.

def elementoP(lista, pos):
    contador = 0
    for elemento in lista:
        if contador == pos:
            return elemento
        contador = contador + 1
    return []


print(elementoP([3,1,4,1],0)) #-> 3
print(elementoP([3,1,4,1],3)) #-> 1
print(elementoP([3,1,4,1],2)) #-> 4
print(elementoP([3,10,4,1],1)) #-> 10
print(elementoP([3,1,4,1],10)) #-> []
print(elementoP([],2)) #-> []