# Objetivo: Regresa Falso o Verdadero si un elemento esta dentro o no de 
# la lista respectivamente
# perteneceq('a', [1,2,3,'a','b']) -> True

def perteneceq(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

print(perteneceq([1,2,3,'a','b'], 'a'))