
from pizza import Pizza # importa la clase Pizza desde pizza.py

print("a. Valores de atributos de clase importada")
print(f"Precio de la pizza: ${Pizza.precio}") #atributo de clase, precio
print(f"Tamaño de la pizza: {Pizza.tamano}")  #atributo de clase, tamaño

print("\nb.  Usar el método estático validar sin crear una instancia (staticmethod)")
elemento = "salsa de tomate"
lista = ["salsa de tomate", "salsa bbq"]
print(f"¿'{elemento}' se encuentra en {lista}? {Pizza.validar(elemento, lista)}")

print("\nc. Crear una instancia y llamar al método (funcion) hacer_pedido")
print("\n--- Realizar un pedido de pizza ---")
mi_pizza = Pizza() # Crea una instancia de la clase Pizza
mi_pizza.hacer_pedido() # Llama al método de instancia para solicitar el pedido al usuario

print("\nd. Mostrar atributos de instancia y validar  y si esa instancia es una pizza válida o no.")
print("\n--- Detalles de la pizza ordenada ---")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")  #instancia.atributo_de_instancia
print(f"Primer ingrediente vegetal: {mi_pizza.ingrediente_vegetal1}") #instancia.atributo_de_instancia
print(f"Segundo ingrediente vegetal: {mi_pizza.ingrediente_vegetal2}")
print(f"Tipo de masa: {mi_pizza.tipo_masa}")
print(f"¿Es una pizza válida? {mi_pizza.es_pizza_valida}")

print("\n e.mostrar si es valida sin crear instancia: no se puede leer atributo si objeto no esta creado")
print(f"¿La clase Pizza es una pizza válida? {Pizza.es_pizza_valida}")
