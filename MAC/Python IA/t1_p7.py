import random

cont = 0

# Con decimales
while cont < 11:
    print(random.uniform(0,10))
    cont += 1

# Sin decimales
print("")
cont = 0
while cont < 11:
    print(random.randint(0,10))
    cont += 1