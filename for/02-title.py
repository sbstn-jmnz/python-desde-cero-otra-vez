# escribir cada palabra con la primera letra en mayúscula
some_text = "hola inmundo"
# Acumulador
word_one = ""

for letter in some_text:
  if letter == 'h':
    word_one += letter.upper()
  elif letter == 'i':
    word_one += letter.upper()
  else:
    word_one += letter

print(word_one)