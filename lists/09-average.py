# Calcular el promedio del siguiente arreglo y mostrar el resultado en la terminal
numbers = [14,52,54,64,76,23,5,2,54,6,32]

total = 0

for number in numbers:
  total += number

print(f"El promedio es: {total/len(numbers)}")
