# Objetivo: Funcion que recibe una lista de listas y regresa la suma de esas listas
# ejemplos: print(sumalistas([[7,4,3],[1,2,3],[6,4]])) ->,[14,6,10]
# print(sumalistas([[],[4,2,3],[6,4,6,1]])) ->,[0,9,17]

def sumalista(lista):
    resultado = 0
    for elemento in lista:
        resultado += elemento
    return resultado

def sumalistas(lista):
    resultado = []
    for sublista in lista:
        resultado = resultado + [sumalista(sublista)]
    return resultado
        


print(sumalistas([[],[4,2,3],[6,4,6,1]]))