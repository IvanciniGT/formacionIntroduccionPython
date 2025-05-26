texto = str("hola") # Dato de tipo str
numero = 10 # Dato de tipo int
numero = int( "10" )
#print(numero)

valor_logico = bool( "true" ) # Dato de tipo bool
#print(valor_logico)

valor_logico= False
valor_logico= bool()
#print(type(valor_logico)) # False

lista = [1,2,3]

lista=list( (1,2,3) )

### Vamos a crear nuestro propio tipo de datos.
# Receta de cocina
# Qué caracteriza a una receta?
# - Nombre del plato
# - Una lista de ingredientes
# - Un procedimiento
# - Un tiempo de preparación
# - Dificultad
# - Porciones
# - Tipo de plato

# Puedo poner una receta en valorAbsoluto?
# Y elevarla al cuadrado?
# Saber si cae en bisiesto?
# Imprimirla bonita? ******
# escalarIngredientesParaUnNumeroDeComensalesEspecifico? ******

from enum import IntEnum

class Dificultad(IntEnum):
    ALTA = 3
    MEDIA = 2
    BAJA = 1

    def __str__(self):
        resultado = "Baja"
        if self == Dificultad.ALTA:
            resultado = "Alta"
        elif self == Dificultad.MEDIA:
            resultado = "Media"
        return resultado

class TipoPlato(IntEnum):
    UNICO = 1
    PRIMERO = 2
    SEGUNDO = 3
    POSTRE = 4
    ENSALADA = 5
    ASADO = 6
    SOPA = 7
    PASTA = 8

    def __str__(self):
        return str(self.name).title()

class Ingrediente:

    def __init__(self, nombre, cantidad, unidad):
        self.nombre = nombre      # Todos estos datos, se guardan en un diccionario, asociado al objeto.
                                  # Podemos acceder a ese diccionario a través de la propiedad __dict__
        self.cantidad = cantidad
        self.unidad = unidad

    def __str__(self):
        return f"{self.cantidad} {self.unidad} de {self.nombre}" # String interpolation

    def escalar(self, factor_escalado):
        return Ingrediente(self.nombre, self.cantidad * factor_escalado, self.unidad)

# Me voy a definir mi nuevo tipo de dato
class Receta:

    def __init__(self, nombre, tiempo=1, dificultad=Dificultad.BAJA, porciones=2, tipo_plato=TipoPlato.PRIMERO, ingredientes=[], procedimiento=[]):
        self.nombre = nombre.upper()
        self.tiempo = tiempo
        self.dificultad = dificultad
        self.porciones = porciones
        self.tipo_plato = tipo_plato
        self.ingredientes = ingredientes
        self.procedimiento = procedimiento

    def escalar_ingredientes(self, numero_de_comensales):
        #ingredientes_escalados = []
        #factor_escalado = numero_de_comensales / self.porciones
        #for ingrediente in self.ingredientes:
        #    ingrediente_escalado = Ingrediente(ingrediente.nombre, ingrediente.cantidad * factor_escalado, ingrediente.unidad)
        #    ingredientes_escalados.append(ingrediente_escalado)
        #return ingredientes_escalados
        ## Vamos a resolver lo mismo con programación funcional. Lo que vamos a aplicar es un modelo MapReduce
                  # map
                  # vvv
        return list(map(lambda ingrediente: ingrediente.escalar(numero_de_comensales / self.porciones), self.ingredientes))
              # ^^^
               #reduce
    def imprimir(self):
        print("="*40)
        print("Receta de: " + self.nombre)
        print("="*40)
        print("Tiempo de preparación: " + str(self.tiempo) + " minutos")
        print("Dificultad: " + str(self.dificultad))
        print("Porciones: " + str(self.porciones))
        print("Tipo de plato: " + str(self.tipo_plato))
        print("-"*40)
        if(len(self.ingredientes)==0):
            print("No hay ingredientes")
        else:
            print("Ingredientes: ")
            for ingrediente in self.ingredientes:
                print(" - " + str(ingrediente))
        print("-"*40)
        print("Procedimiento: ")
        for paso in self.procedimiento:
            print(" - " + paso)
        print("-"*40)

    def __str__(self):
        return "Receta de: " + self.nombre + "\n" + \
               "Tiempo de preparación: " + str(self.tiempo) + " minutos\n" + \
               "Dificultad: " + str(self.dificultad) + "\n" + \
               "Porciones: " + str(self.porciones) + "\n" + \
               "Tipo de plato: " + str(self.tipo_plato) + "\n" + \
               "-"*40

# Una vez tengo un tipo de dato definido.. puedo empezar a crear datos de ese tipo
receta_de_tortilla_de_papatas = Receta(
                                            nombre = "Tortilla de patatas",
                                            tiempo = 30,
                                            dificultad = Dificultad.MEDIA,
                                            porciones = 4,
                                            tipo_plato = TipoPlato.UNICO,
                                            ingredientes = [
                                                Ingrediente("Patatas", 4, "unidades"),
                                                Ingrediente("Huevos", 4, "unidades"),
                                                Ingrediente("Cebolla", 1, "unidad"),
                                                Ingrediente("Aceite de oliva", 100, "ml"),
                                                Ingrediente("Sal", 1, "cucharadita")
                                            ],
                                            procedimiento = ["Pelar las patatas", "Cocinar las patatas", "Batir los huevos", "Mezclar todo", "Cocinar la mezcla"]
                                       )
receta_de_tortilla_de_papatas.imprimir()

ingredientes_para_12_comensales = receta_de_tortilla_de_papatas.escalarIngredientes(12)
print("Ingredientes para 12 comensales:")
for ingrediente in ingredientes_para_12_comensales:
    print(" - " + str(ingrediente))
#print(str(receta_de_tortilla_de_papatas))

#int  33 98
# Hay una cosa que necesitamos MEMORIZAR. Cuando ejecutamos uan función como esas:
# Receta() o similar, python lo que hace es ejecutar una función
# que debe estar definida dentro de la clase a la que estamos llamando:
# __init__(self)
# Esa función recibe un argumento al menos: self.
# Pero ese argumento NO LO PASAMOS NOSOTROS al escribir Receta()
# Python crea un dato al escribir nosotros Receta() y pasa en automático ese dato a la función __init__
# como valor de self
# Ese argumento self representa el ALMA/la ENTIDAD nueva que estamos creando.

# Imprime el tipo de datos del objeto al que apunta la variable receta_de_tortilla_de_papatas
#print(type(receta_de_tortilla_de_papatas))
#print(type(33))

