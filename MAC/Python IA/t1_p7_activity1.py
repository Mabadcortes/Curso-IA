# Piedra, papel o tijera.

import random
print("¿Piedra, papel o tijera?")
mano = random.randint(0,2)

match mano:
    case(0):
        print("Piedra")
    case(1):
        print("Papel")
    case(2):
        print("Tijera")
