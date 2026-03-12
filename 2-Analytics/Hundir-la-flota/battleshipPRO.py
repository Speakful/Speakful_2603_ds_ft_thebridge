# CREAMOS UN TABLERO 10x10 RELLENO DEL CARÁCTER ESPACIO " "

import numpy as np
import random

def crea_tablero(lado = 10):
    tablero = np.full((lado,lado)," ")
    return tablero

# Crea la función `colocar_barcos(tablero)'tablero, que deberá de colocar la lista de barcos generados de forma aleatoria (6 barcos en total (3 barcos de eslora 2, 2 de eslora 3 y 1 eslora 4)) 
# ¡Mucho ojo con barcos que estén superpuestos (no pueden ocupar dos barcos la misma casilla) o barcos que se salgan del tablero!

def coloca_barco_plus(tablero, barco):
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            print(f"Las coordenadas {pieza} no son válidas")
            return False
        if columna <0 or columna>= num_max_columnas:
            print(f"Las coordenadas {pieza} no son válidas")
            return False
        if tablero[pieza] != " ":
            print(f"Las coordenadas {pieza} no son válidas")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    
    while True:
       
        barco = []

        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        print("Intenta colocar otro barco")

# RECIBE UN DISAPRO EN UNO DE LOS BARCOS, SUSTITUYENDO LA 0 POR UNA X

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] != " " and tablero[coordenada] != "X" and tablero[coordenada] != "-":
        tablero[coordenada] = "X"
        print("Impacto :) !")
        return tablero
    elif tablero[coordenada] == "X" or tablero[coordenada] == "-":
        print("Ya disparaste aquí...")
        return None
    else:
        tablero[coordenada] = "-"
        print("Agua :( ! ")
        return tablero
    
def disparo_aleatorio(tablero):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    while True:
        disparo = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))

        if tablero[disparo] != " " and tablero[disparo] != "X" and tablero[disparo] != "-":
            tablero[disparo] = "X"
            print("Impacto ! :)")
            return tablero
        elif tablero[disparo] == "X" or tablero[disparo] == "-":
            pass 
        else: 
            tablero[disparo] = "-"  
            print("Agua ! :(")
            return tablero
