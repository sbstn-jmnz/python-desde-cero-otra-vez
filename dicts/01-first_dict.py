# Un diccionario es similar a las listas, pero que los indices pueden ser cualquier otro tipo de valor.
# En los diccionarios a los indices de les dice llaves o keys

# Ejemplo:
empty_list = {}

# El par de la llave y su valor es un item del diccionario
english_to_spanish = {"one":"uno", "two": "dos"}

print(english_to_spanish["one"]) # => uno
print(english_to_spanish["two"]) # => dos

# Para agregar un nuevo item al diccionario, lo hacemos de la siguiente forma:
english_to_spanish["hello"] = "hola"
english_to_spanish["bye"] = "chao"

print(english_to_spanish)

# El largo del diccionario lo obtenemos igual que con las listas o arreglos
print(len(english_to_spanish))