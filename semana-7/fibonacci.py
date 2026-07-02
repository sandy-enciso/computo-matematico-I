# Calcula el n numero de fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13

def fibonacci(n):
    a = 0
    b = 1
    i = 1
    while i < n:
        b, a = a + b, b 
        i += 1
    return a

print(fibonacci(4))