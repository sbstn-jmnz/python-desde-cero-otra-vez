# Algunas funciones que hemos visto reciben parámetros.
# Por ejemplo print recibe como parámetro lo que va a mostrar en la terminal

def print_hero(hero_name):
  print(f"Soy el súper heroe {hero_name}")

print_hero("Mega Man")

hero = "Chapulín colorado"

print_hero(hero)

# Las funciones que reciben parámetros, estos son obligatorios
# La siguiente sentencia da un error porque falta el parámetro hero_name
print_hero()