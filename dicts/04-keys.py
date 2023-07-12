english_to_spanish = {"one":"uno","two":"dos"}

# Al igual que con .values(), tenemos el .keys(), que retorna un listado de las llaves

keys = english_to_spanish.keys() # => ["one","two"]

for key in keys:
  print(f"{key} => {english_to_spanish[key]}")