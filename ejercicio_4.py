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
