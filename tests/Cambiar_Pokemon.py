
def cambiar_pokemon(entrenador,elegido):
    """
        n = 0
        for pokemon in entrenador.lista_equipo:
            print ("\n Pokemon (", n+1, "): ", pokemon.nombre)
            n += 1
        print ("Si quieres cancelar pulsa 0")
    """

    while True:

        if elegido == 1:
            #Poner mensaje de pokemon ya selecionado
            continue

        elif elegido == 2:
            pokemon_anterior = entrenador.lista_equipo[0]
            entrenador.lista_equipo[0] = entrenador.lista_equipo[1]
            entrenador.lista_equipo[1] = pokemon_anterior

            #Llamar mensaje de pokemon cambiado y actualizar texto
            break

        elif elegido == 3:
            pokemon_anterior = entrenador.lista_equipo[0]
            entrenador.lista_equipo[0] = entrenador.lista_equipo[2]
            entrenador.lista_equipo[2] = pokemon_anterior

            # Llamar mensaje de pokemon cambiado y actualizar texto
            break

        elif elegido == 4:
            pokemon_anterior = entrenador.lista_equipo[0]
            entrenador.lista_equipo[0] = entrenador.lista_equipo[4]
            entrenador.lista_equipo[4] = pokemon_anterior

            # Llamar mensaje de pokemon cambiado y actualizar texto
            break

        elif elegido == 0:

            break

