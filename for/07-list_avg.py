# Calcular el promedio de los números en el arreglo numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

total = 0

for number in numbers:
  total += number

average = total/len(numbers)

print(average)

