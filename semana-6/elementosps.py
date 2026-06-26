# Objetivo: Implemente la función elementosPs que regresa una lista de elementos listae de una lista de posiciones listap. 
# La función recibe dos argumentos: la lista y la lista de posiciones listap. 
# La función regresa una lista.

def elementosPs(lista, listap):
    resultado = []
    for pos in listap:
        contador = 0
        for elemento in lista:
            if contador == pos:
                resultado = resultado + [elemento]
            contador = contador + 1
    return resultado


print(elementosPs([3,1,4,1],[0,2])) # -> [3,4]
print(elementosPs([3,1,4,1],[1,3])) # -> [1,1]
print(elementosPs([3,1,4,1],[2])) # -> [4]
print(elementosPs([3,10,4,1,5],[0,2,4])) # -> [3,4,5]
print(elementosPs([3,1,4,1],[0,10])) # -> [3]
print(elementosPs([],[2,5])) # -> []