
class FiguraGeometrica:

    def area(self):
        pass
    
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)


rectangulo1 = Rectangulo(10, 5)
print(f"Area: {rectangulo1.area()}")
print(f"Perímetro: {rectangulo1.perimetro()}")

rectangulo1.base = 20
print(f"Nuevo área: {rectangulo1.area()}")
print(f"Nuevo perímetro: {rectangulo1.perimetro()}")

#class Cuadrado: # Esto sería una definición VALIDA DE Cuadrado.
#    
#    def __init__(self, lado):
#        self.lado = lado
#
#    def area(self):
#        return self.lado ** 2
#    
#    def perimetro(self):
#        return 4 * self.lado

# Un cuadrado es un objeto de 4 lados iguales, y 4 ángulos de 90 grados, que se caracteriza por un tamaño determinado de lado.
# Pero no es la única definición de Cuadrado que existe: Un cuadrado es un Rectángulo con base y altura iguales.

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)  # Se crea como un rectangulo al que le hubiera pasado como base: lado, y como altura, lo mismo.
                                      # Lo que hago es delegar la construcción del objeto a la clase Rectangulo, con los datos adecuados.

# Y YA! No tengo porque definir los métodos area y perimetro, porque ya los tengo definidos en la clase Rectangulo.
# Y como un Cuadrado es un Rectangulo, hereda todos sus métodos y atributos.

cuadrado1 = Cuadrado(10)
print(f"Area del cuadrado: {cuadrado1.area()}")
print(f"Perímetro del cuadrado: {cuadrado1.perimetro()}")

# RESUMEN: Puedo definir unos tipos de datos basándome en otros, y heredar sus atributos y métodos.
# Este concepto en programación orientada a objetos se llama HERENCIA.
# Podemos decir: El cuadrado hereda de Rectangulo sus atributos y métodos.
#                La clase cuadrado extiende la clase Rectangulo.
#                Es decir, un Cuadrado es un Rectangulo con algunas peculiaridades.

class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio

# Qué tienen en común un Circulo y un Rectangulo?
# Porque habíamos dicho que un Cuadro era un tipo de Rectangulo
# Ambos dos son figuras geométricas, y tienen en común que se les puede calcular el área y el perímetro.
# Cómo se calcula el área y el perímetro de una figura geométrica? NPI... depende de la figura concreta que sea.
# Lo que si sé es que a cualquier figura geométrica se le debe poder calcular el área y el perímetro.

#class FiguraGeometrica:

#    def area(self):
#         pass
    
#    def perimetro(self):
#        pass
# Esta clase define el concepto de figura geométrica, y define los métodos que debe tener cualquier figura geométrica.
# Aporta código? Explica cómo se calcula el área y el perímetro de una figura geométrica? No.

# Una clase como esa, que no aporta código, sino que sólo define los métodos que deben los objetos de este tipo es 
# lo que se llama una INTERFAZ.
# En algunos lenguajes de programación, como Java, se define una interfaz con la palabra clave "interface".


#Eso me permitiría definir por ejemplo una función que imprima los datos de una figura geométrica.

def imprimir_datos_figura(figura: FiguraGeometrica):
    print("Los datos de la figura son:")
    print(f"- Área: {figura.area()}")
    print(f"- Perímetro: {figura.perimetro()}")
    print()

circulo1 = Circulo(5)
cuadrado1 = Cuadrado(10)
rectangulo1 = Rectangulo(10, 5)

figuras = [circulo1, cuadrado1, rectangulo1]
for figura in figuras:
    imprimir_datos_figura(figura)

# RESUMEN: Una interfaz es lo mismo que definir un objeto... pero sin entrar en detalle...
# Es como una sustantivo genérico.
# ARBOL

# PINO: Tipo de árbol con cosas concretas: Las hojas de un pino son aciculares, y el tronco es recto.
# CEREZO: Tipo de árbol con cosas concretas: Las hojas de un cerezo son caducas, y el tronco es retorcido.


# Un circulo es una implementación de la interfaz FiguraGeometrica.
# Un rectangulo es una implementación de la interfaz FiguraGeometrica.
# Un cuadrado es una extensión de la clase Rectangulo, que a su vez es una implementación de la interfaz FiguraGeometrica.