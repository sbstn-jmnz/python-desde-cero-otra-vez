from time import sleep

def print_lyrics():
  print("Hola, hola, hola")
  sleep(1)
  print("¿Como estás?")
  sleep(1)
  print("Yo muy bien")
  sleep(1)
  print("¿Y tú que tal?")

# Imprimir 2 veces
def print_twice():
  print_lyrics()
  print_lyrics()

print_twice()