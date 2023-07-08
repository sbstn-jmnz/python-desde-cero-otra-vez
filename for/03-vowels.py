# Imprimir el siguiente texto con todas las vocales en mayúsculas
some_text = "hola inmundo"

word = ""

for letter in some_text:
  if letter in ['a','e','i','o','u']:
    word += letter.upper()
  else:
    word += letter

print(word)