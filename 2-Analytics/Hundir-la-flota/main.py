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

while True:

    tablero_CPU_oculto = np.where(tablero_CPU == "[O]", "[ ]", tablero_CPU)
    print("PLAYER 1")
    print("")
    print(tablero_PLAYER_1)
    print("")
    print("="*63)
    print("")
    print("CPU")
    print("")
    print(tablero_CPU_oculto)
    print("")
    print("="*63)
    print("")

    while True:

        fila = int(input("Introduce la fila: "))
        columna = int(input("Introduce la columna: "))
        if fila < 0 or fila > 9 or columna < 0 or columna > 9:
            print("")
            print("Coordenadas fuera del tablero ! Introduce un número del 0 al 9")
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


