# Utilizando for y range imprimir los números del 1 al 10, uno en cada fila

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# .....

for num in range(1,11):
  row = ""
  for digit in range(1,num+1):
    row += str(digit)
  print(row)