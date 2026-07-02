# Factorial

def factorial(n):
    resultado = 1
    while n != 0:
        resultado = resultado * n
        n -= 1
    return resultado
    
print(factorial(4)) #24