# %%
from utils import *

# %%
# 1 CREAMOS LOS 2 TABLEROS

tablero_PLAYER_1 = crea_tablero(10)

tablero_CPU = crea_tablero(10)

# %%
# 2) COLOCAR BARCOS EN CADA TABLERO

tablero_PLAYER_1 = crea_barco_aleatorio(tablero_PLAYER_1, eslora=2)
tablero_PLAYER_1= crea_barco_aleatorio(tablero_PLAYER_1, eslora=2)
tablero_PLAYER_1 = crea_barco_aleatorio(tablero_PLAYER_1, eslora=2)
tablero_PLAYER_1 = crea_barco_aleatorio(tablero_PLAYER_1, eslora=3)
tablero_PLAYER_1 = crea_barco_aleatorio(tablero_PLAYER_1, eslora=3)
tablero_PLAYER_1 = crea_barco_aleatorio(tablero_PLAYER_1, eslora=4)

tablero_CPU = crea_barco_aleatorio(tablero_CPU, eslora=2)
tablero_CPU= crea_barco_aleatorio(tablero_CPU, eslora=2)
tablero_CPU = crea_barco_aleatorio(tablero_CPU, eslora=2)
tablero_CPU = crea_barco_aleatorio(tablero_CPU, eslora=3)
tablero_CPU = crea_barco_aleatorio(tablero_CPU, eslora=3)
tablero_CPU = crea_barco_aleatorio(tablero_CPU, eslora=4)

# %%
# 3) LOOP -> WHILE TRUE

turno = 0 # inicio contador de turno 

while True:

    tablero_CPU_oculto = np.where(tablero_CPU == "[O]", "[ ]", tablero_CPU) # crea un tablero oculto de la CPU en donde modifica las "[O]" por "[ ]" (no cheating)
    
    print(f"Turno {turno + 1}") # display del contador de turnos
    print() # separador de líneas

    print("PLAYER 1") # representa el tablero de PLAYER 1
    print("") # separador de líneas

    print(f"{0:>3}" + "".join([f"{i:>3}" for i in range(1, 10)])) # lista del 1 al 9 // con .JOIN unímos la lista -> el índice 0 con un spacing de 3 y el resto con uno de 3
    
    for index, row in enumerate(tablero_PLAYER_1): # FOR loop para enumerar las filas -> enumerate -> índice = posición (0,1,2..) // row = enumera la fila
            print(index, end = "") 
            for cell in row: #para cada celda en fila x
                if cell == "[X]": # IF loop para cambiar el color de las celdas cuando se recibe impacto
                    print("\033[91m" + "[X]" + "\033[0m", end = "") # cambia el color a rojo // "rojo" + "texto" + "factory reset"
                elif cell == "[-]": # si no es "[X]" -> revisar si es "[-]"
                    print("\033[94m" + "[-]" + "\033[0m", end = "") # cambia el color a azul // "azul" + "texto" + "factory reset"
                else: # si no es "[X]" ni "[-]" -> devuelve la celda normal 
                    print(cell, end = "")
            print()
        
    print("") # separador de líneas
    print("="*55) # separador de líneas
    print("") # separador de líneas
    
    print("CPU") # representa el tablero de CPU
    print("") # separador de líneas

    print(f"{0:>3}" + "".join([f"{i:>3}" for i in range(1, 10)])) # lista del 1 al 9 // con .JOIN unímos la lista -> el índice 0 con un spacing de 6 y el resto con uno de 6
    
    for index, row in enumerate(tablero_CPU_oculto): # FOR loop para enumerar las filas -> enumerate -> índice = posición (0,1,2..) // row = enumera la fila
            print(index, end = "")
            for cell in row:
                if cell == "[X]":
                    print("\033[91m" + "[X]" + "\033[0m", end = "") # cambia el color a rojo // "rojo" + "texto" + "factory reset"
                elif cell == "[-]":
                    print("\033[94m" + "[-]" + "\033[0m", end = "") # cambia el color a azul // "azul" + "texto" + "factory reset"
                else:
                    print(cell, end = "")
            print()
  
    print("") # separador de líneas
    print("="*55) # separador de líneas
    print("") # separador de líneas

    while True:

        fila = int(input("Latitud: "))
        columna = int(input("Longitud "))
        print("")
        if fila < 0 or fila > 9 or columna < 0 or columna > 9: #IF loop para no permitir coordenadas fuera del tablero // el loop continua hasta que el usuario introduce coordenadas válidas
            print("")
            print("Coordenadas fuera del tablero ! Introduce un número del 0 al 9") # indica al usuario el rango de coordenadas
            print("")
            continue

        lat_long = (fila, columna)

        target = (recibir_disparo(tablero_CPU, lat_long))

        if target is not None: 
            tablero_CPU = target
            break

    if len(tablero_CPU[tablero_CPU == "[O]"]) == 0: 
        print("Winner Winner Chicken Dinner !!!")
        break

    # disparo_aleatorio PLAYER 1 VS CPU

    tablero_PLAYER_1 = disparo_aleatorio(tablero_PLAYER_1)

    if len(tablero_PLAYER_1[tablero_PLAYER_1 == "[O]"]) == 0:
        print("Uuuuuuuuuh perdiste")
        break

    turno += 1 # tras revisar ambas win condition y ver que el juego sigue -> turno + 1


