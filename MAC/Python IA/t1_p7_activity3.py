# Piedra, papel o tijera al mejor de 1 en python.
import random

victoriasJugador = 0
victoriasMaquina = 0 

while victoriasJugador < 3 and victoriasMaquina < 3:
    print("")
    print("Victorias jugador = " + str(victoriasJugador))
    print("Victorias máquina = " + str(victoriasMaquina))
    print("Introduce la mano que desea sacar:")
    print("1- Piedra")
    print("2- Papel")
    print("3- Tijera")
    manoJugador = int(input())
    manoMaquina = random.randint(1,3)

    match manoJugador:
        case 1:
            if manoJugador == manoMaquina:
                print("Habeis sacado los dos piedra, habéis empatado")
            elif manoMaquina == 2:
                print("La máquina ha sacado papel, ha ganado la máquina")
                victoriasMaquina += 1
            elif manoMaquina == 3:
                print("La máquina ha sacado tijera, ha ganado el jugador")
                victoriasJugador += 1
        case 2:
            if manoJugador == manoMaquina:
                print("Habeis sacado los dos papel, habéis empatado")
            elif manoMaquina == 3:
                print("La máquina ha sacado tijera, ha ganado la máquina")
                victoriasMaquina += 1
            elif manoMaquina == 3:
                print("La máquina ha sacado piedra, ha ganado el jugador")
                victoriasJugador += 1
        case 3:
            if manoJugador == manoMaquina:
                print("Habeis sacado los dos tijera, habéis empatado")
            elif manoMaquina == 1:
                print("La máquina ha sacado piedra, ha ganado la máquina")
                victoriasMaquina += 1
            elif manoMaquina == 2:
                print("La máquina ha sacado papel, ha ganado el jugador")
                victoriasJugador += 1

if victoriasJugador == 3:
    print("El jugador ha ganado la partida!!")
else:
    print("La máquina ha ganado la partida!!")