#primera clase coder numeros y cadenas de caracteres
print("hola mundo bienvenidos")
#este es un ejersiscio de numeros en python,donde range es el rango de los numeros 
[print(i) for i in range(1, 5)]
#mismo ejemplo pero del 1 al 5 ya que el 6 no vapor que se pone hasta un elemento menos
[print(i)for i in range(1, 4)]
#cadenas de caracteres 
# Crear una cadena de caracteres
cadena = "Hola Mundo"

# Acceder a un carácter específico de la cadena
print(cadena[0])  # Imprime 'H'

# Concatenar cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
concatenada = cadena1 + " " + cadena2
print(concatenada)  # Imprime "Hola Mundo"

# Reemplazar parte de una cadena
cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Hola", "Adiós")
print(nueva_cadena)  # Imprime "Adiós Mundo"

# Dividir una cadena en una lista
cadena = "Hola Mundo"
lista_palabras = cadena.split()
print(lista_palabras)  # Imprime ['Hola', 'Mundo']

# Obtener la longitud de una cadena
cadena = "Hola Mundo"
longitud = len(cadena)
print(longitud)  # Imprime 10

# Convertir una cadena a minúsculas
cadena = "Hola Mundo"
cadena_minusculas = cadena.lower()
print(cadena_minusculas)  # Imprime "hola mundo"

# Convertir una cadena a mayúsculas
cadena = "Hola Mundo"
cadena_mayusculas = cadena.upper()
print(cadena_mayusculas)  # Imprime "HOLA MUNDO"
