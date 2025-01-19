#Funcion para definir si un año es biciesto o no
def es_bisiesto(año):
    return (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0)

#Funcion para contar los años desde el año ingresado hasta 1900
def contar_años_bisiestos(año):
    if año < 1900:
        años_totales = 1900 - año + 1
        bisiestos = (años_totales // 4) - (años_totales // 100) + (años_totales // 400)
    else:
        años_totales = año - 1900 + 1
        bisiestos = (años_totales // 4) - (años_totales // 100) + (años_totales // 400)
    return bisiestos

# Funcion principal del programa
año = int(input("Ingrese un año: "))
print(f"Número de años bisiestos entre {año} y 1900: {contar_años_bisiestos(año)}")
