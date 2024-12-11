# Piedra, papel o tijera al mejor de 1.
import random

def piedraPapelTijera(manoJugador):
    manoMaquina = random.randint(1,3)

    match manoJugador:
        case 1:
            if manoJugador == manoMaquina:
                print("Habeis sacado los dos piedra, habéis empatado")
            elif manoMaquina == 2:
                print("La máquina ha sacado papel, ha ganado la máquina")
            elif manoMaquina == 3:
                print("La máquina ha sacado tijera, ha ganado el jugador")
        case 2:
            if manoJugador == manoMaquina:
                print("Habeis sacado los dos papel, habéis empatado")
            elif manoMaquina == 3:
                print("La máquina ha sacado tijera, ha ganado la máquina")
            elif manoMaquina == 3:
                print("La máquina ha sacado piedra, ha ganado el jugador")
        case 3:
            if manoJugador == manoMaquina:
                print("Habeis sacado los dos tijera, habéis empatado")
            elif manoMaquina == 1:
                print("La máquina ha sacado piedra, ha ganado la máquina")
            elif manoMaquina == 2:
                print("La máquina ha sacado papel, ha ganado el jugador")

print("Introduce la mano que desea sacar:")
print("1- Piedra")
print("2- Papel")
print("3- Tijera")
manoJugador = int(input())

piedraPapelTijera(manoJugador)
