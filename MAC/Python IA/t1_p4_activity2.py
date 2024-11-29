# Diseña un programa en Python que te devuelva tu horóscopo 
# ingresando tu día y mes de nacimiento (en número entero).
# Día y mes deben ser ingresados como número entero.

print("Introduce tu dia de nacimiento")
dia = int(input())

print("Introduce el número del mes de tu nacimiento")
mes = int(input())

match mes:
    case(1):
        if dia <= 20:
            cadena = "Tu horóscopo es Capricornio"
        else:
            cadena = "Tu horóscopo es Acuario"
    case(2):
        if dia <= 19:
            cadena = "Tu horóscopo es Acuario"
        else:
            cadena = "Tu horóscopo es Piscis"
    case(3):
        if dia <= 20:
            cadena = "Tu horóscopo es Piscis"
        else:
            cadena = "Tu horóscopo es Aries"
    case(4):
        if dia <= 20:
            cadena = "Tu horóscopo es Aries"
        else:
            cadena = "Tu horóscopo es Tauro"
    case(5):
        if dia <= 20:
            cadena = "Tu horóscopo es Tauro"
        else:
            cadena = "Tu horóscopo es Geminis"
    case(6):
        if dia <= 20:
            cadena = "Tu horóscopo es Geminis"
        else:
            cadena = "Tu horóscopo es Cáncer"
    case(7):
        if dia <= 22:
            cadena = "Tu horóscopo es Cáncer"
        else:
            cadena = "Tu horóscopo es Leo"
    case(8):
        if dia <= 23:
            cadena = "Tu horóscopo es Leo"
        else:
            cadena = "Tu horóscopo es Virgo"
    case(9):
        if dia <= 22:
            cadena = "Tu horóscopo es Virgo"
        else:
            cadena = "Tu horóscopo es Libra"
    case(10):
        if dia <= 23:
            cadena = "Tu horóscopo es Libra"
        else:
            cadena = "Tu horóscopo es Escorpio"
    case(11):
        if dia <= 22:
            cadena = "Tu horóscopo es Escoprio"
        else:
            cadena = "Tu horóscopo es Sagitario"
    case(12):
        if dia <= 21:
            cadena = "Tu horóscopo es Sagitario"
        else:
            cadena = "Tu horóscopo es Capricornio"


print(cadena)
