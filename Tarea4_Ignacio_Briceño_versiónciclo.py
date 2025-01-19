#Funcion para verificar si un año es biciesto o no
def es_bisiesto(año):
    return (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0)

#Ciclo(bucle) que cuenta desde el año puesto hasta 1900
def contar_años_bisiestos(año):
    conteo_bisiestos = 0
    if año >= 1900:
        for i in range(1900, año + 1):
            if es_bisiesto(i):
                conteo_bisiestos += 1
    else:
        for i in range(año, 1900 + 1):
            if es_bisiesto(i):
                conteo_bisiestos += 1
    return conteo_bisiestos

#Parte principal del programa, esto le pide a la persona colocar el año de entrada
año = int(input("Ingrese un año: "))
print(f"Número de años bisiestos entre {año} y 1900: {contar_años_bisiestos(año)}")
