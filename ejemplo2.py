
"""saludar funcion"""
import os
def limpiar_terminal():
    os.system("cls")
limpiar_terminal()

def saludar(nombre):
    print(f"hola, {nombre}, como estas? ya comiste?")
name=input("digite el nombre: ")
saludar(nombre)

"""#saludar ("zeus")"""