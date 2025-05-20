
# Operadores

## Operadores que podemos aplicar sobre números

### Operadores aritméticos

2+3    # 5
2-3    # -1
2*3    # 6
2/3    # 0.6666666666666666
2//3   # 0
2%3    # 2
2**3   # 8


# Operadores de comparación básicos: Se pueden aplicar a cualquier tipo de dato
2 == 3  # False
2 != 3  # True
                    ## vvvvv  Se pueden aplicar sobre números y textos
2 > 3   # False
2 < 3   # True
2 >= 3  # False
2 <= 3  # True

"hola" > "adios" # True Cuando se aplican estos operadores sobre textos se mira el orden lexicográfico

# a < b < c < h

## Operadores lógicos

True and False # True
True or False  # True
not True       # False

# Operadores sobre textos
# +  -> Concatenación
"hola " + "mundo" # "hola mundo"
# *  -> Repetición
"hola " * 3 # "hola hola hola "


# Operadores de asignación

numero = 4
# Operadores aritméticos de asignación
numero +=  3 # numero = numero + 3
numero -=  3 # numero = numero - 3
numero *=  3 # numero = numero * 3
numero /=  3 # numero = numero / 3
numero //= 3 # numero = numero // 3
numero %=  3 # numero = numero % 3
numero **= 3 # numero = numero ** 3


# Operadores de pertinencia

# in
"hola" in "hola mundo"  # True
23 in [1,2,3,4,5]       # False
77 in [11,22,33,44,55,66,77] # True