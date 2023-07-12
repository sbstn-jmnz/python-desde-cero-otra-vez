# Hacer un diccionario que tenga tres items. 
# python: Lenguaje moderno utilizado para todo tipo de aplicaciones
# ruby: Lenguaje completamente orientado a objetos  
# js: lenguaje para la web y los servidores

lenguaje = input("¿Qué lenguaje quieres conocer? ")

lenguajes = {}

lenguajes["python"] = "Python is a programming language that lets you work more quickly and integrate your systems more effectively."
lenguajes["ruby"] = "Ruby is an interpreted, high-level, general-purpose programming language which supports multiple programming paradigms."
lenguajes["javascript"] = "JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web,"

if lenguaje in lenguajes:
  print(f"Sí está {lenguaje}")
  print(f"Su valor es: {lenguajes[lenguaje]}")
else:
  print(f"No conozco el lenguaje {lenguaje}")