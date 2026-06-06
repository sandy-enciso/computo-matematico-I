# Fibonacci

# 0 1 1 2 3 5 8 13

def crea_lista_aux(n,conta):
    if n == 0:
        return []
    else:
        return [conta] + crea_lista_aux(n-1, conta+1)
    
def crea_lista(n):
    return crea_lista_aux(n,0)


def fibonacci(n):
    a = 0 # 1 1 2
    b = 1 # 1 2 3

    for i in crea_lista(n):
        b, a = b + a, b

    return a

print(fibonacci(6))

print(crea_lista(0))