texto = "   Hola amiguete !!!   "

print("El texto tiene", len(texto), "caracteres")
print("Las primeras 5 letras son", texto[:5])

# Otras operaciones sobre textos

## Control del case
print("El texto en mayúsculas es", texto.upper())
print("El texto en minúsculas es", texto.lower())
print("El texto en modo título es", texto.title()) # Capitaliza la primera letra de cada palabra
print("El texto en modo frase es", texto.capitalize()) # Capitaliza la primera letra de la cadena
print("El texto al revés es", texto.swapcase()) # Cambia el case de cada letra


## control de espacios en blanco
print("El texto sin espacios es", "XX",texto, "XX") # Elimina los espacios en blanco al principio y al final
print("El texto sin espacios es", "XX",texto.strip(),"XX") # Elimina los espacios en blanco al principio y al final
print("El texto sin espacios a la izquierda es", "XX",texto.lstrip(),"XX") # Elimina los espacios en blanco al principio
print("El texto sin espacios a la derecha es", "XX",texto.rstrip(),"XX") # Elimina los espacios en blanco al final


# Split...parte un texto en trozos... que se añaden a una lista(tupla)

texto="2,3,4,5,67,89,10"
valores = texto.split(",") # Separa el texto en una lista de valores
print("Los valores son", valores)
print("El tercer valor es", valores[2])
print("Contiene el 89",  "89" in valores )
print("Posicion en la que aparece  el 89",  valores.index("89") )