def turno_aliado(entrenador, tipo_enemigo, hp_enemigo, def_enemigo):
    while True:

        accion = int(
            input(print("¿Que accion quieres realizar?: \n (1): Cambiar de aliado \n (2): Usar objeto \n (3): Atacar")))

        # # CAMBIAR # #
        if accion == 1:
            cambiar_pokemon(entrenador)


        # # OBJETOS # #
        elif accion == 2:
            objeto = int(input("¿Quieres huir o curarte?: \n (1): Huir \n (2): Pociones"))

            #### Cuerda Huida ####
            if objeto == 1:

                # Si tiene en el inventario
                if (entrenador.inventario["cuerda_huida"] > 0):

                    # Si consigue huir
                    if (huir()):

                        entrenador.inventario["cuerda_huida"] = entrenador.inventario["cuerda_huida"] - 1
                        print("Has huido con exito")
                        return True # Salir del bucle

                    # Si no consigue huir
                    else:

                        entrenador.lista_equipo["cuerda_huida"] = entrenador.inventario["cuerda_huida"] - 1
                        print("No has conseguido huir")

            #### Pocion ####
            elif objeto == 2:

                entrenador.lista_equipo[0].HP = pocion(entrenador.lista_equipo[0].HP, entrenador.lista_equipo[0].HP_MAX)


        # #  ATACAR # #
        elif accion == 3:

            hp_enemigo = atacar(entrenador.lista_equipo[0].equipo, hp_enemigo, def_enemigo, tipo_enemigo,
                                entrenador.lista_equipo[0].tipo)
            return False     #Salir del bucle

        # #  ERROR # #
        else:
            print("Elige una opcion valida")







def combate(entrenador, tipo_enemigo, hp_enemigo, def_enemigo, ataque_enemigo):

    #Bucle principal
    while True:




        #Ataque enemigo
        if (hp_enemigo != 0):
            entrenador.lista_equipo[0].HP = atacar(ataque_enemigo, entrenador.lista_equipo[0].HP, entrenador.lista_equipo[0].defensa, entrenador.lista_equipo[0].tipo, tipo_enemigo)

        elif (hp_enemigo == 0):
            print ("Has ganado el combate")
            #Añadir experiencia
            break





        #Si el aliado sigue con vida
        if (entrenador.lista_equipo[0].HP != 0):

            if (turno_aliado(entrenador, tipo_enemigo, hp_enemigo, def_enemigo)): break    #Si ha huido
            else: continue                                                                 #Si no ha huido


        #Si el aliado no sigue con vida
        elif (entrenador.lista_equipo[0].HP == 0):

            print ("Aliado eliminado")
            #Retirar al pokemon
            entrenador.lista_muertos.append(entrenador.lista_equipo[0]) #Meter en la lista de muertos
            entrenador.lista_equipo.pop(entrenador.lista_equipo[0])     #Retirar del equipo de aliado

            #Si quedan aliados vivos
            if (len(entrenador.lista_equipo[0] != 0)):

                turno_aliado(entrenador, tipo_enemigo, hp_enemigo, def_enemigo)

            #No quedan aliados vivos
            else:

                print ("Todos tus aliados han muerto, has perdido el combate")
                break
