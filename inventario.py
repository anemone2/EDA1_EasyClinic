import pandas as pd
import random as rdm

# Nombres son mas como IDs

itemsPicos = {
    'nombre':['pico_diamante', 'pico_oro', 'pico_hierro','pico_piedra','pico_madera'],
    'valor':[10, 20, 30, 40, 50],
    'probabilidad':[5, 15, 30, 50, 100], # Este numero presenta un rango: 0-5 (5), 6-15 (10), 16-30 (15), 30-50 (20), 50-100 (50) (igual y luego lo quito del dict)
}

def randItem():
    num = rdm.randint(0, 100) 
    # print(str(num)) mi debugger boneto
    if num <= 5: print("Pico de diamante! ")
    elif num > 5 and num <= 15: print("Pico de oro! ")
    elif num > 15 and num <= 30: print("Pico de hierro! ")
    elif num > 30 and num <= 50: print("Pico de piedra. " )
    elif num > 5 and num <= 100: print("Pico de madera. :( ")

# TODO: por que putas a veces no genera los cuatro items. ni puta idea!!

randItem()
randItem()
randItem()
randItem()
