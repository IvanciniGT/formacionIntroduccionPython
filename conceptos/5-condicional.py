
nombre = input( "Escribe tu nombre: ") # Statement
edad = input( "Escribe tu edad:  ")
## Saludarle
print( "Hola " + nombre + ". Tienes " + edad + " años.")

# if EXPR_BOOLEANA:
#     CODIGO QUE DEBE EJECUTARSE SI LA EXPRESION BOOLEANA ES VERDADERA
# elif EXPR_BOOLEANA2:
#     CODIGO QUE DEBE EJECUTARSE SI LA EXPRESION BOOLEANA2 ES VERDADERA pero LA PRIMERA NO
# else:
#     CODIGO QUE DEBE EJECUTARSE SI NINGUNA DE LAS ANTERIORES ES VERDADERA

if int(edad) >= 100:
    print( "Por lo tanto eres un superviviente!") 
elif int(edad) >= 18:
    print( "Por lo tanto eres mayor de edad")
else:
    if int(edad) >= 0:
        print( "Por lo menos has nacido")  # Statement (Sentencia ~ Frase)
    else:
        print( "Estás en proyecto")

# Siempre que pongo 2 puntos, indica que comienza un sub-bloque de código. 
# Y debo empezar en la linea de abajo hacia la derecha.
# Cuanto?

# En python hay un OPERADOR (Ein??=?= Esos no los estabamos viendo en el fichero 3-operadores ???)
# Que sirve para condicionales. El operador ternario de python.

#        valor_si_verdadero    if   EXPR_BOLEANO        else    valor_si_falso
#         "mayor"              if   int(edad) >= 18     else        "menor"

#         En muchos otros lenguajes solemos esriobir:   
#                                   EXPR_BOLEANO ? valor_si_verdadero : valor_si_falso

print("Eres "+ ("mayor" if int(edad) >= 18 else "menor") + " de edad")

