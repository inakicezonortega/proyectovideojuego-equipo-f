
def cambiar_pokemon(entrenador):

    n = 0
    for pokemon in entrenador.lista_equipo:
        print ("\n Pokemon (", n+1, "): ", pokemon.nombre)
        n += 1
    print ("Si quieres cancelar pulsa 0")


    while True:
        elegido = int(input("¿Con cual quieres pelear?"))

        if elegido == 1:
            print ("Ya combates con ese Pokemon")
            continue

        elif elegido == 2:
            pokemon_anterior = entrenador.lista_equipo[0]
            entrenador.lista_equipo[0] = entrenador.lista_equipo[1]
            entrenador.lista_equipo[1] = pokemon_anterior

            print ("Ahora combates con:", entrenador.lista_equipo[0].nombre)
            break

        elif elegido == 3:
            pokemon_anterior = entrenador.lista_equipo[0]
            entrenador.lista_equipo[0] = entrenador.lista_equipo[2]
            entrenador.lista_equipo[2] = pokemon_anterior

            print ("Ahora combates con:", entrenador.lista_equipo[0].nombre)
            break

        elif elegido == 4:
            pokemon_anterior = entrenador.lista_equipo[0]
            entrenador.lista_equipo[0] = entrenador.lista_equipo[4]
            entrenador.lista_equipo[4] = pokemon_anterior

            print ("Ahora combates con:", entrenador.lista_equipo[0].nombre)
            break

        elif elegido == 0:
            print ("EXIT")
            break

        else:
            print ("Elige un valor valido")
            continue