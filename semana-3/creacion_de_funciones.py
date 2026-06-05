# Definicion de funciones en Python

def nombre(lista_de_parametros):
    print("sentencia 1")
    print("sentencia 2")
    print("sentencia n")


def cuadrado(x): return x*x

def cubo(x): return x*x*x

print('cuadrado de 5: ' + str(cuadrado(5)))

print('cubo de 2: ' + str(cubo(2)))

def promedio(a,b,c,d):
    suma=a+b+c+d
    return suma/4.0

print('ejemplo promedio: ' + str(promedio(10,8,7,10)))