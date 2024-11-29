
print ("Introduce tu nombre: ")
nombre = input()

# Calculadora Simple

print("Bienvenid@ a nuestra CALCU " + nombre)
print("\nIntroduce el primer dígito ENTERO: ")
n1 = int(input())

print("Introduce el segundo dígito ENTERO: ")
n2 = int(input())

print("Introduce la operación a realizar ( +, - , *, / )")
operacion = input()
valid = True

if operacion == "+":
    resultado = n1 + n2
elif operacion == "-":
    resultado = n1 - n2
elif operacion == "*":
    resultado = n1 * n2
elif operacion == "/":
    resultado = n1 / n2
else:
    print("Introduce un valor correcto")
    valid = False

if valid == True :
    cad = "{} {} {} = {}".format(n1, operacion, n2, resultado)
    print("La operación elegida es " + cad)

