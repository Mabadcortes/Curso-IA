# ACTIVIDAD: Cálculo de áreas simples.
import math


print("Cálculo de áreas:")
print("-----------------")
print("1 - Cuadrado")
print("2 - Rectángulo")
print("3 - Triángulo")
print("4 - Círculo")
opcion = int(input())

match opcion:
    case(1):
        print("Introduce el lado del cuadrado: ")
        lado = int(input())
        print("El área del cuadrado es {}".format(lado*lado))
    case(2):
        print("Introduce la base del rectángulo: ")
        base = int(input())
        print("Introduce la altura del rectángulo: ")
        altura = int(input())
        print("El área del rectángulo es {}".format(base*altura))
    case(3):
        print("Introduce la base del triángulo: ")
        base = int(input())
        print("Introduce la altura del triángulo: ")
        altura = int(input())
        print("El área del triángulo es {}".format(((base*altura)/2)))
    case(4):
        print("Introduce el radio del círculo: ")
        radio = int(input())
        print("El área del círculo es {}".format(math.pi * (radio * radio)))
