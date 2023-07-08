# Los slices son como rebanadas de una lista o segmentos y se utilizan con el símbolo :

letters = ['a','b','c','d','e','f','g']
# Parte en el primero y termina en el indice previo del último
# En este caso seleccionará desde el índice uno al dos
print(letters[1:3])

print(letters[:4])

print(letters[3:])

# Con los slices también podríamos modificar varios valores

letters[1:3] = ['x','y']
print(letters)