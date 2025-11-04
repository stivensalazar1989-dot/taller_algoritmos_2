
import os
def limpiar_terminal():
    os.system("cls")
limpiar_terminal()

def resta(a,b,c,d):
    
    return (a-b-c-d)
print("programa principal")
a=float(input("ingrese el primer numero: "))
b=float(input("ingrese el segundo numero: "))
c=float(input("ingrese el tercer numero: "))
d=float(input("ingrese el cuarto numero: "))
print(f" el resultado de la suma es: {resta(a,b,c,d)}")