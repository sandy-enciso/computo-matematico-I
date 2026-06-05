import math

def imprimeLogaritmo(x):
    if x <= 0:
        print('Sólo números positivos por favor')
        return
    result = math.log(x)
    print('El logaritmo de ', x, 'es',result)

imprimeLogaritmo(4)