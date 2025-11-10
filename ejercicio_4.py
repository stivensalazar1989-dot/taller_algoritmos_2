#ejercicio numero 4
"""Desarrolla un programa que determine el grupo etario de una persona según su edad. 
Crea una función llamada obtener_grupo_etario que reciba un número entero correspondiente a la edad y 
devuelva una cadena que indique si la persona es: "Niño" (0–12 años), "Adolescente" (13–17 años), "Adulto" (18–64 años) o 
"Adulto mayor" (65 años o más). 

La función debe verificar que la edad no sea negativa; si lo es, debe devolver un mensaje de error como "Edad no válida". 
Luego, implementa una función mostrar_clasificacion que reciba el nombre (cadena de texto) y la edad (entero) de una persona,
y muestre un mensaje en pantalla indicando a qué grupo etario pertenece, por ejemplo: "Lucía es un(a) Adulto". 
"""


#limpiar terminal
import os
def limpiar_terminal():
    os.system('cls')  # Para Windows
limpiar_terminal()

# funciona creada para determina la edad ingresada
def obtener_grupo_etario(edad):
    if edad < 0:
        return "Edad no válida"
    elif edad <= 2:
        return "bebe"
    elif edad <= 11:
        return "Niño"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:
        return "Adulto mayor"

# Funcion creada para saber en que grupo esta la persona ingresada
def resultado_final(nombre, edad):
    grupo = obtener_grupo_etario(edad)
    print(f"{nombre} es un(a) {grupo}" if grupo != "Edad no válida" else f"{nombre}: {grupo}")# respuesta en terminal del resultado 

# datos solicitados al cliente
nombre = input("Ingresa el nombre de la persona: ")

while True:
    try:
        edad = int(input("Ingresa la edad de la persona: "))
        if edad < 0:
            print("Edad no válida. Intenta nuevamente.")
        else:
            break
    except ValueError:
        print("Debes ingresar un número entero. Intenta nuevamente.")# respuesta en terminal del resultado 

# Mostrar clasificación final
resultado_final(nombre, edad)


