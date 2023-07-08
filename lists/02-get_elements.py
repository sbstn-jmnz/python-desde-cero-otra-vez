# La sintaxis para acceder a los elementos es con el nombre de la variable que tiene la listas seguida de los corchetes [] con su índice al interior

fruits = ["apple","orange","pineapple"]
print(fruits[0])

# Los elementos en una lista tienen una posición numérica partiendo desde el 0

# Las listas son modificables, es decir, pueden mutar. En otras palabras las listas con mutables, a diferencia de los strings que son inmutables.

fruits[0] = "chocolate"

print(fruits)

# Ejemplo, los strings son inmutables, es decir una vez que se establece su valor, este no se puede modificar

some_string = "Mundo"

print(some_string[0])

# La siguiente sentencia es un error. Los string no se pueden modificar
# some_string[0] = "X"

print(some_string)

# Los indices de las listas se pueden reemplazar por cualquier expresión que entregue un entero que está dentro de los índices definidos

import random

print(fruits[random.randint(0,len(fruits)-1)])

# Si el indice es un valor negativo, cuenta de atrás hacia adelante

print(fruits[-2])

# Siempre el último elemento se puede acceder mediante el número -1
print(fruits[-1])