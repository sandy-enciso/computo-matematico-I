# elimina varios elementos a partir de una lista dada. 
# La función recibe dos argumentos: la lista y la lista de elementos listae que se desean eliminar. 
# La función regresa la lista con los elementos eliminados.

def porEliminar(elemento, lista):
    for i in lista:
        if elemento == i:
            return True
    return False


def eliminaVE(lista, elementos_por_eliminar):
    resultado = []
    for elemento in lista:
        if not porEliminar(elemento, elementos_por_eliminar):
            resultado = resultado + [elemento]        
    return resultado

print(eliminaVE([3,1,4,1],[3,4])) #  -> [1,1]
print(eliminaVE([3,1,4,1],[1,4])) # -> [3]
print(eliminaVE([3,1,4,1],[2,5])) # -> [3,1,4,1]
print(eliminaVE([3,10,4,1,5],[3,4,5])) # -> [10,1]
print(eliminaVE([],[2,5])) # -> []