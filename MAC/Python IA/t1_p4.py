# Crea un programa que lea el día de la semana de la persona 
# (como una cadena de texto) y responda con una actividad habitual para ese día.

print("Introduce el nº del día de la semana (1 al 7):")
diaSemana = int(input())

cadena = ''

def switchSemana(diaSemana):
    match diaSemana:
        case(1):
            return("La actividad para el lunes es Fútbol")
        case(2):
            return("La actividad para el martes es Natación")
        case(3):
            return("La actividad para el miercoles es Baloncesto")
        case(4):
            return("La actividad para el jueves es Golf")
        case(5):
            return("La actividad para el viernes es Pasear")
        case(6):
            return("La actividad para el sabado es Descansar")
        case(7):
            return("La actividad para el domingo es Atletismo") 

cadena = switchSemana(diaSemana)
print(cadena)


match diaSemana:
    case(1):
        print("La actividad para el lunes es Fútbol")
    case(2):
        print("La actividad para el martes es Natación")
    case(3):
        print("La actividad para el miercoles es Baloncesto")
    case(4):
        print("La actividad para el jueves es Golf")
    case(5):
        print("La actividad para el viernes es Pasear")
    case(6):
        print("La actividad para el sabado es Descansar")
    case(7):
        print("La actividad para el domingo es Atletismo")

