# La forma más común de recorrer una lista es utilizando el loop for.

some_list = ["code", "terminal", "linux", "git"]

for elem in some_list:
  print(elem)

# Lo anterior funciona bien si solo queremos utilizar los valores que ya existe. Pero si necesitamos actualizar algún valor necesitaremos los indices

numbers = [1,2,3,4,5,6,7,8,9,10]

# Si queremos multiplicar cada elemento de la lista por 2, debemos utilizar también los indices
for index in range(len(numbers)):
  numbers[index] = numbers[index] * 2

print(numbers)
