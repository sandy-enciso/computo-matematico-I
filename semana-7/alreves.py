# Objetivo: Invertir los elementos de una lista

def alreves(lista):
    resultado = []
    while lista != []:
        resultado = [lista[0]] + resultado
        lista = lista[1:]
    return resultado

print(alreves([1,2,3,4,5])) # [5,4,3,2,1]