# Funciones anonimas

def cuadrado(n): return n * n

print(cuadrado(5))

print((lambda n: n * n)(5))

def multiplica(a,b): return a * b

print(multiplica(2,3))

print((lambda a, b: a * b)(2,3))


# Imaginen que se tiene la funcion llamada mimap
# mimap(funcion, lista)
# Aplica la funcion que recibe como primer argumento
# a cada elemento de la lista que recibe como segundo argumento

# mimap(cuadrado, [1,2,3,4]) -> [1,4,9,16]
# mimap(lambda x: x*x, [1,2,3,4]) -> [1,4,9,16]
# mimap(lambda x: x*x*x*x, [1,2,3,4]) -> [1,16,...]

# Las funciones lambda se utilizan cuando solo queremos ussar la funcion una sola vez en ese momento
