# Plato del día
# Un programa que pida por teclado el día de la semana
# Y que te diga cuál es el plato del día
from random import *

print("Introduce cuantos días de la semana quieres consultar su plato del día")
numDias = int(input())
cont = 0
days = []
cadena = ''

while cont < numDias:
    print("Introduce el día de la semana que quieras consultar su plato del día: ")
    day = input()
    days.append(day)
    cont +=1

comidas = ["Macarrones", "Pizza", "Albóndigas", "Croquetas", "Puchero", "Hamburguesa", "Paella"]

i = 0
while i < numDias: 
    numRandom = randint(0,6)
    cadena = cadena + "\nEl plato del día para el {} es {}".format(days[i],comidas[numRandom])
    i += 1

print(cadena)
