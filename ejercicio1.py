#ejercicio numero 1
"""Crea un programa donde implementes una función para calcular las principales operaciones aritméticas de dos números, 
la función tendrá tres parámetros ( operación, num1, num2 ) 
y debe devolver el resultado de la operación aritmética indicada en el argumento . 
Deberás tener en cuenta la división por cero (“Error  División por Cero”). 
"""
import os


def limpiar_terminal():
    os.system("cls")


limpiar_terminal()


def calcular(operacion, num1, num2):
    if operacion == "suma":
        return num1+num2
    elif operacion == "resta":
        return num1-num2
    elif operacion == "multiplicacion":
        return num1*num2
    elif operacion == "division":
        return num1/num2
    if num2 == 0:
        print("error division entre cero::INF")
    else:
        return num1/num2


print("programa principal")

operacion = input(
    "ingrese la operacion que desee realizar: suma /resta /multiplicacion /divicion: ").lower()
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
print(calcular(operacion, num1, num1))


