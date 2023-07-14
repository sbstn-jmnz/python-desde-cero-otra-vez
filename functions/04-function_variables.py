# Las funciones pueden definir variables en su interior, pero estas variables son parte de se ámbito y no son accesibles desde fuera de la función

def print_fullname(firstname,lastname):
  fullname = f"{firstname} {lastname}"
  print(f"---- {fullname} ------")

print_fullname("Seba", "Jmnz")

# Desde afuera no podemos acceder a las variables internas de la función
print(fullname)