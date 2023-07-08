# Dibujar una x de tamaño 12 utilizando el *
# *               *
#   *           *
#     *       *
#       *   *
#         *
#       *   *
#     *       *
#   *           *
# *               *


for y in range(1,12):
  line = ""
  for x in range(1,12):
    if (x == y) or (x + y == 12):
      line += "*"
    else:
      line += " "
  print(line)