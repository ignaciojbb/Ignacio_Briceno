def obtener_ingredientes():
    print("Ingrese las cantidades de los ingredientes:")
    tazas_agua = float(input("Tazas de agua: "))
    tazas_harina = float(input("Tazas de harina PAN: "))
    cucharaditas_sal = float(input("Cucharaditas de sal: "))
    cucharadas_aceite = float(input("Cucharadas de aceite: "))

    return tazas_agua, tazas_harina, cucharaditas_sal, cucharadas_aceite

def calcular_volumen(tazas_agua, tazas_harina, cucharaditas_sal, cucharadas_aceite):
    cucharadas_agua = tazas_agua * 16
    cucharadas_harina = tazas_harina * 16
    cucharaditas_aceite = cucharadas_aceite * 3

    volumen_total_cucharaditas = (cucharadas_agua * 3) + (cucharadas_harina * 3) + cucharaditas_sal + cucharaditas_aceite
    volumen_total = volumen_total_cucharaditas / 48  

    volumen_final = volumen_total * 0.9  

    return volumen_final

def convertir_tazas_a_gramos(tazas, gramos_por_taza):
    return tazas * gramos_por_taza

def convertir_tazas_a_cm3(tazas):
    cm3_por_taza = 240
    return tazas * cm3_por_taza

tazas_agua, tazas_harina, cucharaditas_sal, cucharadas_aceite = obtener_ingredientes()

volumen_final_tazas = calcular_volumen(tazas_agua, tazas_harina, cucharaditas_sal, cucharadas_aceite)

gramos_por_taza_harina = 120
volumen_harina_gramos = convertir_tazas_a_gramos(tazas_harina, gramos_por_taza_harina)
volumen_final_cm3 = convertir_tazas_a_cm3(volumen_final_tazas)


print(f"El volumen final de la arepa terminada es: {volumen_final_tazas:.3f} tazas")
print(f"El volumen de harina usado es: {volumen_harina_gramos:.3f} gramos")
print(f"El volumen final de la arepa terminada es: {volumen_final_cm3:.3f} cm³")