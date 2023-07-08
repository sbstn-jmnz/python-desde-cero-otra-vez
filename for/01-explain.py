# Podemos utilizar el for para recorrer cada letra de un texto
# y realizar alguna evaluación condicional por cada letra

some_text = "Hola Inmundo"

word_one = ""

for letter in some_text:
  if letter == " ":
    word_one += "\n"
  else:
    word_one += letter

print(word_one)