size = int(input("¿De qué tamaño quieres el cuadrante?"))

for row in range(size):
  line = ""
  for col in range(size):
    line += f"({row},{col})"
  print(line)