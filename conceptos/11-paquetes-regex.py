# Expresiones regulares?

# Las expresiones regulares son una forma de identificar patrones en cadenas de texto.
# Nos ayudan a:
# - Saber si una cadena de texto cumple con un patrón
# - Extraer partes de una cadena de texto que cumplen con un patrón
# - Reemplazar partes de una cadena de texto que cumplen con un patrón
# - Dividir una cadena de texto en partes que cumplen con un patrón

# Los patrones de expresiones regulares los solemos definir con una sintaxis que se introdujo en un lenguaje 
# de programación antiguo.. hoy en día poco usado, que se llama Perl.
# Esa sintaxis que definió perl para patrones es muy cómoda.. y se ha exportado a todos los lenguajes de programación.

# PATRON = CONJUNTO DE SUBPATRONES
# SUBPATRON = Conjunto de caracteres + Modificador de cantidad

# Conjunto de caracteres:                                                   COINCIDENCIAS
#                                                                            hola amigo
#      hola                    literalmente hola                             1111
#                                                                            hola amigo
#      [hola]                  cualquiera de las letras h, o, l, a           1234 5   6
#      [a-z]                   cualquier letra entre la a-z
#      [A-Z]                   cualquier letra entre la A-Z
#      [0-9]                   cualquier letra entre el 0-9
#      [a-zA-Z]                cualquier letra entre la a-z o A-Z
#      [0-9a-zA-Z]             cualquier letra entre el 0-9 o a-z o A-Z
#      [0-9a-zA-ZñÑáéíoúj.-]
#      .                       cualquier carácter

# Modificadores de cantidad:
#       nada                    1 vez
#       ?                       0 o 1 vez (OPCIONAL)
#       *                       0 o más veces
#       +                       1 o más veces
#       {n}                     n veces
#       {n,}                    n o más veces
#       {n,m}                   entre n y m veces

# Además tenemos otros caracteres iomportantes:
#    \            Escapar el siguiente carácter
#    $    Fin de línea
#    ^    Inicio de línea
#    ()   Agrupar subpatrones
#    |    OR entre subpatrones


# Patrón: Identificar números del 1 al 299

#        [1-299]      Eso sería : El 1 o el 2 o el 9
# Los números del 1 al 9:           [1-9]
# Los números del 10 al 99:         [1-9][0-9]
# Los números del 100 al 299:       2[0-9][0-9]

# ([1-9][0-9]?)|([12][0-9][0-9])

# Python permite trabajar con expresiones regulares.. pero la funcionalidad de expresiones regulares no se activa de serie.
# Hay que activarla (importarla) para poder usarla.
# Esa funcionalidad se recoge en lo que llamamos un paquete/módulo.
# Python, trae de serie muchos paquetes/módulos, que de entrada están desactivados.
# Pero podemos usarlos, importándolos.
# Además, otras personas / empresas han creado paquetes/módulos que podemos usar.
# En ese caso primero debemos instalar el paquete/módulo y luego importarlo.

# En el caso que nos ocupa, python incluye la funcionalidad de expresiones regulares en un
# paquete/módulo que se llama re.

# Para usar el paquete re, primero lo importamos:
import re
# Y luego podemos usar las funciones que nos ofrece.
#re.search() # Busca un patrón en una cadena de texto
#re.match()  # Busca un patrón al principio de una cadena de texto
#re.findall() # Busca todas las coincidencias de un patrón en una cadena de texto

# Por ejemplo: Quiero saber si un texto cumple con un patrón: Primera letra en mayúscula y el resto en minúscula

patron = r"^[A-Z][a-z]+$"
nombre = "Federico"
# quiero saber si nombre cumple con el patrón
if(re.match(patron, nombre)):
    print("El nombre cumple con el patrón")
else:
    print("El nombre no cumple con el patrón")

# Un módulo es un paquete de Clases, Enumerados, Funciones, Variables, etc. que puede ser usado en un programa.

from re import match

if(match(patron, nombre)):
    print("El nombre cumple con el patrón")

if(match(patron, nombre)):
    print("El nombre cumple con el patrón")

if(match(patron, nombre)):
    print("El nombre cumple con el patrón")

if(match(patron, nombre)):
    print("El nombre cumple con el patrón")            