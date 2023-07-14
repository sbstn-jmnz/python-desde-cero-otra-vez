# Crear una función que imprima cada elemento de la lista fruits
# de le siguiente forma I like xxxxxxx

fruits = ["apple","orange","kiwi","banana"]
more_fruits = ["watermelon","mango","pineapple","pear"]


def print_fruits(fruits_list):
  for fruit in fruits_list:
    print(f"I like {fruit}")

print_fruits(fruits)
print_fruits(more_fruits)
