#ejercicio numero 3
""" Escribe un programa que calcule el total a pagar en un restaurante incluyendo una propina. 
Para ello, crea una función llamada calcular_propina que reciba dos parámetros: 
el monto de la cuenta (un número decimal) y el porcentaje de propina (también un número decimal),
 y devuelva el valor de la propina. Luego, diseña otra función llamada total_con_propina 
 que utilice la función anterior para sumar el monto de la cuenta y la propina, devolviendo 
 el total a pagar. Finalmente, crea una función mostrar_total que reciba el monto de la cuenta y 
 el porcentaje de propina, y que imprima el subtotal, el valor de la propina y el total a pagar, 
 todos con formato de dos decimales. """

#limpiesa de terminal
import os
def limpiar_terminal():
    os.system("cls")
limpiar_terminal()




def calcular_propina(monto, porcentaje):
    # monto:valor de la cuenta
    # porcentaje: porcentaje de propina 
    propina = monto * (porcentaje / 100)
    return propina

def total_con_propina(monto, porcentaje):
    #calcula el total sumando la propina
    propina = calcular_propina(monto, porcentaje)
    total = monto + propina
    return total

def mostrar_total(monto, porcentaje):
    #muestra los resultados con dos decimales
    propina = calcular_propina(monto, porcentaje)
    total = total_con_propina(monto, porcentaje)

    #imprime lo que se le va mostrar al cliente
    print(f"subtotal: ${monto:.2f}")
    print(f"propina ({porcentaje}%): ${propina:.2f}")
    print(f"total a pagar: ${total:.2f}")
   

# programa principal
monto = float(input("ingrese el monto de la cuenta: "))
porcentaje = float(input("ingrese el porcentaje de propina (%): "))
#variable total
mostrar_total(monto, porcentaje)

