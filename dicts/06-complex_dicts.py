# Podemos utilizar todas las otras estructuras de datos para combinarlas de forma de representar información más compleja

recipes_book = {
  "pollo al horno": {
    "ingredients": ["Un pollo entero","1 cebolla","2 dientes de ajo","1 zanahoria"],
    "steps": "Lavar los trozos de pollo, secar y sazonar con sal y Pimienta Blanca Molida Gourmet.En una olla profunda calentar el aceite y dorar las presas de pollo por ambos lados. Retirar y reservar.En la misma olla, freír a fuego bajo la cebolla, zanahorias y pimentones; hasta que la cebolla esté transparente y las verduras blandas (aprox. 10 minutos). Luego agregar la hoja de Laurel Gourmet y Mix de pimientas. Para hacer el caldo de pollo disolver el sobre en agua y revolver. Incorporar las presas de pollo, el caldo de pollo y el vino. Corregir la sazón, llevar a ebullición, reducir el calor y cocinar por 15 a 20 minutos o hasta que el pollo esté cocinado. Al final agregar las arvejas. Servir caliente acompañado de papas fritas, arroz o lo que guste."
  },
  "carne al jugo": {
    "ingredients": ["800 gramos de tapapecho","1 Cebolla","2 dientes de ajo","una pizca de sal"],
    "steps":"Sacar el exceso de grasa de la carne. Calentar un sartén  y derretir la mantequilla. Agregar la maicena disuelta en agua fría y la cebolla. Cocinar hasta dorar. Mover la cebolla a un lado y meter la carne. Condimentarla por ambos lados con el Condimento para Carne y con la Sal de Mar. Sellar. Agregar las zanahorias y agua caliente hasta cubrir la carne.Agregar el Caldo en Polvo de Costilla, las Hojas de Laurel y el vino tinto. Revolver. Cocinar tapado y a fuego bajo por 2,5 horas. La carne está lista cuando al tocarla se desarma casi sola. Una vez cocida la carne, sacarla de la cacerola y servir."
  },
  "salmon al horno": {
    "ingredients": ["Un filete de salmón fresco","eneldo","sal y limón"],
    "steps": "Calentar el horno a 200°C. Aliñar el salmón con el aliño para pescado y luego poner en una bandeja levemente aceitada junto a los cebollines enteros. Reservar. Preparar la costra de hierbas, mezclando todos los ingredientes. Untar el pescado con la mostaza, luego cubrir con las hierbas y terminar con 1 a 2 rodajas de limón. Rociar con el vino blanco y hornear por 20 a 25 minutos. Servir inmediatamente, acompañar con papas o arroz."
  }
}

meals = recipes_book.keys() # ["pollo al horno", "carne al jugo", "salmon al horno"]

for meal in meals:
  print("--------------")
  print(f"{meal.title()}")
  print("--------------")
  ingredients = recipes_book[meal]["ingredients"]
  for ingredient in ingredients:
    print(f"- {ingredient}")
  
  print(recipes_book[meal]["steps"])
 