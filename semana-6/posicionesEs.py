# Objetivo: determina los índices de los elementos de una lista (listae) en una lista principal (listap).
# La función recibe dos argumentos: la lista principal (listap) y lista de elementos (listae). 
# La función regresa una lista de índices.

def posicionesE(lista, elemento):
    resultado = []
    contador = 0
    for i in lista:
        if i == elemento:
            resultado = resultado + [contador]
        contador = contador + 1
    return resultado

def posicioneses(listap, listae):
    resultado = []
    for elemento in listae:
        posicion = posicionesE(listap, elemento)
        if posicion != []: 
            resultado = resultado + [posicion]
    return resultado



print(posicioneses([3,1,4,1],[1,4])) # -> [[1,3],[2]]
print(posicioneses([3,1,4,1],[2,6])) # -> []
print(posicioneses([3,1,4,1],[1])) # -> [[1,3]]
print(posicioneses([1,1,1,2],[1,2])) # -> [[0,1,2],[3]]
print(posicioneses([1,1,1,2],[])) # -> []
print(posicioneses([],[1,4])) # -> []