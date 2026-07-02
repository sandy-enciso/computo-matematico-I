# Calcula la potencia de un numero

def potencia(a, b):
    resultado = a
    while b > 1:
        resultado = resultado * a
        b -= 1
    return resultado

print(potencia(2,3)) # 8
print(potencia(0,0)) # 0