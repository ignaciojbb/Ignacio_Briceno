#Funcion para definir el nombre
def validar_nombre(nombre):
    if nombre.istitle():
        return True
    else:
        print("El nombre debe comenzar con mayúscula.")
        return False

#Funcion para Definir el sexo
def obtener_sexo():
    sexo = input("Sexo (masculino/femenino): ").strip().lower()
    if sexo in ["masculino", "femenino"]:
        return sexo
    else:
        print("Opción no contemplada. Cerrando el programa.")
        exit()

#Funcion para definir región
def obtener_región():
    opciones_región = ["Sinnoh", "Hoenn", "Unova"]
    print("Regiones disponibles:", ", ".join(opciones_región))
    región = input("Región: ").strip().title()
    if región in opciones_región:
        return región
    else:
        print("Opción no contemplada. Cerrando el programa.")
        exit()

#Función para definir el pokemon favorito de la region 
def pokemon_favorito_de_la_región(región):
    pokemones_favoritos = {
        "Sinnoh": ["Garchomp", "Empoleon", "Bidoof"],
        "Hoenn": ["Sceptile", "Blaziken", "Mudkip"],
        "Unova": ["Haxorus", "Zoroark", "Snivy"]
    }
    print(f"Pokémon favoritos de {región}: ", ", ".join(pokemones_favoritos[región]))
    pokemon_favorito = input("Pokémon favorito: ").strip().title()
    if pokemon_favorito in pokemones_favoritos[región]:
        return pokemon_favorito
    else:
        print("Opción no contemplada. Cerrando el programa.")
        exit()

def main():
    nombre = input("Nombre: ").strip()
    while not validar_nombre(nombre):
        nombre = input("Nombre: ").strip()
    
    sexo = obtener_sexo()
    región = obtener_región()
    pokemon_favorito = pokemon_favorito_de_la_región(región)
    
    if sexo == "femenino":
        pronombre = "ella"
    else:
        pronombre = "él"

    if sexo == "femenino":
        pronombre2 = "entrenadora"
    else:
        pronombre2 = "entrenador"

    if sexo == "femenino":
        pronombre3 = "esta"
    else:
        pronombre3 = "este"
    
    print(f"{nombre} es de {región} y su Pokémon favorito es {pokemon_favorito}.")
    print(f"{pronombre.capitalize()} está comenzando su viaje para ser {pronombre2.capitalize()} pokemon, el compañero mas fiel y primer pokemon de {pronombre3} {pronombre2} es {pokemon_favorito}.")

if __name__ == "__main__":
    main()
