# Objetivo: determina los  ́ındices de un elemento dentro de una lista. 
# La función recibe dos argumentos: la lista y un elemento. La función regresa una lista de índices.
#print(posicionesE([3,1,4,1],1)) # -> [1,3]

def posicionesE(lista, elemento):
    resultado = []
    contador = 0
    for i in lista:
        if i == elemento:
            resultado = resultado + [contador]
        contador = contador + 1
    return resultado


print(posicionesE([3,1,4,1],1))