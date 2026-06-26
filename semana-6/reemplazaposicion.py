# Objetivo: Implemente la función reemplazaposicion que sustituye un elemento que se encuentra en una posición por otro. 
# La función recibe entonces tres argumentos:
# (1) La posición que se quiere reemplazar pos.
# (2) El elemento por el que será reemplazado e y
# (3) La lista donde se desea hacer el reemplazo. La función regresa regresa la lista

def reemplazaposicion(pos, e, lista):
    resultado = []
    contador = 0
    for elemento in lista:
        if contador == pos:
            resultado = resultado + [e]
        else:
            resultado = resultado + [elemento]
        contador = contador + 1
    return resultado

print(reemplazaposicion(0,100,[2,4,3,1,2])) # -> [100, 4, 3, 1, 2]
print(reemplazaposicion(2,82,[2,4,3,1,2])) # -> [2, 4, 82, 1, 2]
print(reemplazaposicion(4,65,[2,4,3,1,2])) # -> [2, 4, 3, 1, 65]