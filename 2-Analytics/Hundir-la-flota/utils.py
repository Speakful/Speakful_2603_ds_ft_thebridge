# %%
# Step 1: Create the Board

import numpy as np
import random

np.set_printoptions(linewidth=200)

# %%
# Step 2: Validate and Place a Ship

def crea_tablero(lado = 10):
    tablero = np.full((lado,lado), "[ ]")
    return tablero

crea_tablero(10)

# %%
def coloca_barco_plus(tablero, barco): #2
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
        if tablero[pieza] != "[ ]":
            print(f"Las coordenadas {pieza} no son válidas")
            return False
        tablero_temp[pieza] = "[O]"
    return tablero_temp

# %%
# Step 3: GENERATE A RANDOM SHIP

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100): #3
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    barcos_id = ["Ranni", "Perla Negra", "Radahn", "Acorazado", "", "Tusk", 
                      "Tank", "Fundador", "Malenia", "Ace", "Colosal", "Seaking"]
    
    while True:
       
        barco = []

        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        print(f"{random.choice(barcos_id)}:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])

        if orientacion == "N":
            print("Proa al norte, a la conquista !")
            print("")
        elif orientacion == "S":
            print("Rumbo sur, hacia aguas desconocidas !")
            print("")
        elif orientacion == "O":
            print("Navegando hacia el este, al horizonte !")
            print("")
        else: 
            print("Virando al oeste, tierra a la vista !")
            print("")

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
        print("")

# %%
# Step 4: HANDLE PLAYER SHOTS
# RECIBE UN DISAPRO EN UNO DE LOS BARCOS, SUSTITUYENDO LA 0 POR UNA X

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] != "[ ]" and tablero[coordenada] != "[X]" and tablero[coordenada] != "[-]":
        tablero[coordenada] = "[X]"
        print("PLAYER 1: Impacto directo, capitán! :)")
        print("")
        return tablero
    elif tablero[coordenada] == "[X]" or tablero[coordenada] == "[-]":
        print("")
        print("PLAYER 1: Ya disparaste aquí... Perdiste el mapa ?")
        print("")
        return None
    else:
        tablero[coordenada] = "[-]"
        print("PLAYER 1: Agua... El mar se traga tu bala sin piedad :(")
        print("")
        return tablero
        
    

# %%
# Step 5: CPU RANDOM SHOT

def disparo_aleatorio(tablero):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    while True:
        disparo = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))

        if tablero[disparo] != "[ ]" and tablero[disparo] != "[X]" and tablero[disparo] != "[-]":
            tablero[disparo] = "[X]"
            print("CPU: Impacto enemigo !")
            print("")
            print("-"*20, "FIN DEL TURNO", "-"*20)
            print("")
            return tablero
        elif tablero[disparo] == "[X]" or tablero[disparo] == "[-]":
            print("CPU: La IA repite coordenadas... Necesita un GPS !")
            pass 
            print("-"*20, "FIN DEL TURNO", "-"*20)
            print("")
        else: 
            tablero[disparo] = "[-]"  
            print("CPU: El enemigo dispara al vacío !")
            print("")
            print("-"*20, "FIN DEL TURNO", "-"*20)
            print("")
            return tablero



# %%
