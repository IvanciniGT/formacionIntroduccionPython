
def mayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    return numero2

#def mayor_otra_opcion(numero1, numero2):
#    return numero1 if numero1 > numero2 else numero2


def mayor_de_tres_numeros(numero1, numero2, numero3): 
    return mayor( mayor(numero1, numero2), numero3 )

print( "El mayor entre 2 y 2 es", mayor(2,2) )