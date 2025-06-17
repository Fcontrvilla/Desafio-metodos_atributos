

ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
tipos_masa = ["tradicional", "delgada"]


class Pizza:
    precio = 10000      #atributo de clase
    tamano = "Familiar" #atributo de clase

    @staticmethod  # metodo estatico  no crea objeto de clase
    def validar(texto:str,casos_posibles:list):  #valida texto en lista de casos posibles
        if texto in casos_posibles:
            return True
        else:
            return False

    def __init__(self):  #inicia atributos para la instancia
        self.ingrediente_proteico = ""
        self.ingrediente_vegetal1 = ""
        self.ingrediente_vegetal2 = ""
        self.tipo_masa = ""
        self.es_pizza_valida = False

    def hacer_pedido(self):   #metodo de instancia
        self.ingrediente_proteico = input(f"Ingrese el ingrediente proteico ({ingredientes_proteicos})").lower()
        es_proteico_valido =Pizza.validar(self.ingrediente_proteico,ingredientes_proteicos)

        self.ingrediente_vegetal1 = input(f"Ingrese el primer ingrediente vegetal ({ingredientes_vegetales}): ").lower()
        es_vegetal1_valido =Pizza.validar(self.ingrediente_vegetal1,ingredientes_vegetales)

        self.ingrediente_vegetal2 = input(f"Ingrese el segundo ingrediente vegetal({ingredientes_vegetales}): ").lower()
        es_vegetal2_valido =Pizza.validar(self.ingrediente_vegetal2,ingredientes_vegetales)

        self.tipo_masa = input(f"Ingrese el tipo de masa ({tipos_masa}): ").lower()
        es_masa_valido =Pizza.validar(self.tipo_masa,tipos_masa)

        if es_proteico_valido == True and es_vegetal1_valido == True and es_vegetal2_valido == True and es_masa_valido == True:
            self.es_pizza_valida = True
        else:
            self.es_pizza_valida = False