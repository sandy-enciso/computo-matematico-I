# Funcion sumalista
# El objetivo es sumar los elementos de una lista

def sumalista(lista):
    suma = 0
    for elemento in lista:
        suma+=elemento

    return suma

print(sumalista([1,2,3,4,5]))
print(sumalista([]))