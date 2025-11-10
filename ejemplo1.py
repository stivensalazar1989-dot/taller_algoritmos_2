#ejercicio numero 2
"""Crea un programa donde implementes una función para contar las vocales y 
consonantes de un texto, palabra o párrafo ingresado, la función debe devolver un mensaje que 
indique el numero de vocales y numero de consonantes del texto ingresado.
"""


#limpiesa de terminal
import os
def limpiar_terminal():
    os.system("cls")
limpiar_terminal()

# Programa: Contar vocales y consonantes

def contar_letras(texto):
    # texto  palabra o frase ingresada por el usuario
    texto = texto.lower()  # Convertimos a minúsculas para simplificar el conteo
    vocales = "aeiou"
    numero_vocales = 0
    numero_consonantes = 0

    # Recorremos cada letra del texto
    for letra in texto:
        if letra.isalpha():  # Verifica que sea una letra (profe, coloque "isalpha" para que el programa quede mas corto y limpo)
            if letra in vocales:
                numero_vocales += 1
            else:
                numero_consonantes += 1

    # retorna un mensaje con los resultados
    return f"El texto tiene {numero_vocales} vocales y {numero_consonantes} consonantes"


# programa principal
texto_usuario = input("ingrese un texto, palabra o parrafo: ")
resultado = contar_letras(texto_usuario)
print(resultado)


