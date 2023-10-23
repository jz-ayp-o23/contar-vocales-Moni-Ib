"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
CONSTANTE = "aeiouáéíóúü"

# Entradas
entrada = input("Introduzca una frase: ")

# Proceso
cantidad_vocales = 0
for letra in entrada:
    if letra.lower() in CONSTANTE:
        cantidad_vocales += 1
        print(f"La frase tiene {cantidad_vocales} vocales")
else: 
    print(f"La frase tiene {cantidad_vocales} vocales")


