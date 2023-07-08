# Python nos da métodos para operar sobre las listas. Por ejemplo podríamos agregar un nuevo elemento al final de la lista con el método append()

letters = ['a', 'b', 'c']
letters.append('x')

print(letters)

# También podemos agregar los elementos de una lista a otra utilizando el método extend()

more_letters = ['m','n','o','p']
letters.extend(more_letters)

print(letters)

numbers = [1,2,3,4]
letters.extend(numbers)

print(letters)

# El método sort() ordena los elementos de forma ascendente
other_letters = ['d','a','e','g','b']
other_letters.sort()
print(other_letters)
