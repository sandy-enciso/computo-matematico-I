# Notas de los programas de `semana-3`

## Conceptos principales

- Paradigma procedural: los programas se organizan como una secuencia de instrucciones que modifican el estado y resuelven un problema paso a paso.
- Iteración: repetir un conjunto de instrucciones para procesar datos. En Python se usa `for`, `while` y otras estructuras repetitivas.
- Predicados en Python: funciones o expresiones que devuelven `True` o `False`.

## Archivos y su propósito

- `first_implementacion.py`: ejemplo de función simple que regresa el primer elemento de una lista. Muestra cómo definir una función y usar retorno directo.
- `rest.py`: función `rest(lista)` que devuelve una lista sin su primer elemento. Ilustra el acceso a sublistas con `lista[1:]`.
- `ultimo.py`: muestra cómo obtener el último elemento de una lista usando una iteración con `for` y construyendo una lista inversa.

- `factorial.py`: implementación de factorial mediante funciones auxiliares y un ciclo `for`. Aquí se usa iteración para multiplicar los elementos de un rango creado con `crea_intervalo`.
- `fibonacci.py`: cálculo de la sucesión de Fibonacci usando una lista de índices y un bucle `for` para actualizar los valores de la serie.
- `potencia.py`: (no se lee en este resumen) probablemente contiene una función para elevar números a una potencia, otro ejemplo típico de procedimiento matemático.

- `suma_lista.py`: suma todos los elementos de una lista con un `for`. Es un ejemplo claro de iteración acumulativa.

- `if_and_return.py`: muestra una función que usa `if` para validar datos, imprime un mensaje de error y usa `return` para detener la ejecución si la condición no se cumple.
- `if_variante_1.py`: ejemplo de sentencia `if` simple que ejecuta un bloque cuando el predicado es verdadero.
- `if_variante_2.py`: ejemplo de `if ... else`, con dos rutas de ejecución según el resultado del predicado.
- `if_variante_3.py`: ejemplo de `if ... elif ... else`, para múltiples condiciones exclusivas.
- `if_variante_4.py`: ejemplo de `if` anidado, que muestra cómo una condición puede contener otra condición dentro del bloque `else`.

- `predicados.py`: contiene ejemplos de comparaciones (`==`, `!=`, `>`, `<`, `<=`, `>=`) y operadores lógicos (`and`, `or`, `not`). Son todos predicados porque su resultado es `True` o `False`.
- `creacion_de_funciones.py` y `ejemplos_de_funciones.py`: muestran cómo crear funciones y reutilizarlas en Python. Son parte del aprendizaje de la estructura procedural.

- La mayoría de los archivos usa el paradigma procedural: se define una función, se ejecuta un bloque de instrucciones y se imprime el resultado.
- La iteración aparece en `for.py`, `factorial.py`, `fibonacci.py`, `suma_lista.py` y `ultimo.py` como el mecanismo para repetir pasos.
- Los predicados se usan en las estructuras `if` y `if_variante_*`, así como en `predicados.py` para entender la lógica booleana.
