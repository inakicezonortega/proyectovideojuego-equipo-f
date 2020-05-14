import random


############## TURNO VS POKEMON ##############

def turno_aliado_p(entrenador, pokemon, accion):
    while True:

        # # CAMBIAR # #
        if accion == 3:
            cambio = True
            while not cambio:
                num = 0
                num += 1


        # # POCION # #
        elif accion == 2:
            entrenador.lista_equipo[0].HP = pocion(entrenador, entrenador.lista_equipo[0].HP,
                                                   entrenador.lista_equipo[0].HP_MAX)


        # # CUERDA HUIDA # #
        elif accion == 4:

            # Si tiene en el inventario
            if entrenador.inventario["cuerda_huida"] > 0:

                # Si consigue huir
                if huir(entrenador):
                    return True  # Salir del bucle


        # #  ATACAR # #
        elif accion == 1:

            pokemon.HP = atacar(entrenador.lista_equipo[0].tipo, pokemon.tipo, pokemon.HP, pokemon.HP_MAX,
                                entrenador.lista_equipo[0].ataque)
            return False  # Salir del bucle


############## TURNO VS ENTRENADOR ##############

def turno_aliado_e(entrenador, rival, accion):
    while True:

        # # CAMBIAR # #
        if accion == 3:
            cambio = True
            while not cambio:
                num = 0
                num += 1


        # # POCION # #
        elif accion == 2:
            entrenador.lista_equipo[0].HP = pocion(entrenador, entrenador.lista_equipo[0].HP,
                                                   entrenador.lista_equipo[0].HP_MAX)


        # # CUERDA HUIDA # #
        elif accion == 4:

            # Si tiene en el inventario
            if entrenador.inventario["cuerda_huida"] > 0:

                # Si consigue huir
                if huir(entrenador):
                    return True  # Salir del bucle


        # #  ATACAR # #
        elif accion == 1:

            rival.lista_equipo[0].HP = atacar(entrenador.lista_equipo[0].tipo, rival.lista_equipo[0].tipo,
                                              rival.lista_equipo[0].HP, rival.lista_equipo[0].HP_MAX,
                                              entrenador.lista_equipo[0].ataque)
            return False  # Salir del bucle


############## COMBATE VS POKEMON ##############

def combate_p(entrenador, pokemon, accion, room_anterior, x_anterior, y_anterior):
    # Bucle principal
    while self.combate:

        # Ataque enemigo
        if pokemon.HP != 0:
            entrenador.lista_equipo[0].HP = atacar(pokemon.tipo, entrenador.lista_equipo[0].tipo,
                                                   entrenador.lista_equipo[0].HP, entrenador.lista_equipo[0].HP_MAX,
                                                   pokemon.ataque)

        # Gana el combate
        elif pokemon.HP == 0:
            entrenador.lista_equipo[0].contador_exp = exp(entrenador.lista_equipo[0].contador_exp,
                                                          entrenador.lista_equipo[0].nivel, pokemon.nivel)

            # Volver a la habitacion anterior
            self.current_room = room_anterior

            # Coordenadas anteriores
            self.player_sprite.center_x = x_anterior
            self.player_sprite.center_y = y_anterior
            break

        # Si el aliado sigue con vida
        if entrenador.lista_equipo[0].HP != 0:

            if turno_aliado_p(entrenador, pokemon, accion):

                # Volver a la habitacion anterior
                self.current_room = room_anterior

                # Coordenadas anteriores
                self.player_sprite.center_x = x_anterior
                self.player_sprite.center_y = y_anterior

                break  # Si ha huido
            else:
                continue  # Si no ha huido


        # Si el aliado no sigue con vida
        elif entrenador.lista_equipo[0].HP == 0:

            # Retirar al pokemon
            entrenador.lista_muertos.append(entrenador.lista_equipo[0])  # Meter en la lista de muertos
            entrenador.lista_equipo.pop(entrenador.lista_equipo[0])  # Retirar del equipo de aliado

            # Si quedan aliados vivos
            if len(entrenador.lista_equipo[0] != 0):

                turno_aliado_p(entrenador, pokemon, accion)

            # No quedan aliados vivos
            else:

                # Volver a la habitacion inicial
                self.current_room = 1

                # Coordenadas iniciales
                self.player_sprite.center_x = 840
                self.player_sprite.center_y = 120

                break


############## COMBATE VS ENTRENADOR ##############

def combate_e(entrenador, rival, accion, room_anterior, x_anterior, y_anterior):
    # Bucle principal
    while self.combate:

        # Ataque enemigo
        if rival.lista_equipo[0].HP != 0:
            entrenador.lista_equipo[0].HP = atacar(rival.lista_equipo[0].tipo, entrenador.lista_equipo[0].tipo,
                                                   entrenador.lista_equipo[0].HP, entrenador.lista_equipo[0].HP_MAX,
                                                   rival.lista_equipo[0].ataque)

        # Ganar el combate
        elif rival.lista_equipo[0].HP == 0:

            # Si quedan enemigos vivos, cambiar el que combate
            if len(rival.lista_equipo[0] != 0):
                rival.lista_muertos.append(rival.lista_equipo[0])  # Añado a la lista de muertos
                rival.lista_equipo.pop(0)  # Retirara de disponibles


            # No quedan enemigos vivos
            else:
                entrenador.lista_equipo[0].contador_exp = exp(entrenador.lista_equipo[0].contador_exp,
                                                              entrenador.lista_equipo[0].nivel,
                                                              rival.lista_equipo[0].nivel)
                # Volver a la habitacion anterior
                self.current_room = room_anterior

                # Coordenadas anteriores
                self.player_sprite.center_x = x_anterior
                self.player_sprite.center_y = y_anterior
                break

        # Si el aliado sigue con vida
        if entrenador.lista_equipo[0].HP != 0:

            if turno_aliado_p(entrenador, rival, accion):
                break  # Si ha huido
            else:
                continue  # Si no ha huido


        # Si el aliado no sigue con vida
        elif entrenador.lista_equipo[0].HP == 0:

            # Retirar al pokemon
            entrenador.lista_muertos.append(entrenador.lista_equipo[0])  # Meter en la lista de muertos
            entrenador.lista_equipo.pop(entrenador.lista_equipo[0])  # Retirar del equipo de aliado

            # Si quedan aliados vivos
            if len(entrenador.lista_equipo[0] != 0):

                turno_aliado_p(entrenador, rival, accion)

            # No quedan aliados vivos
            else:
                # Pierdes el combate, los pokemon enemigos vuelven a su estado inicial
                for pokemon_muerto in rival.lista_muertos:
                    pokemon_muerto.HP = pokemon_muerto.HP_MAX  # Cura al pokemon
                    rival.lista_equipo.append(pokemon_muerto)  # Lo añade a los disponibles
                    rival.lista_muertos.pop(pokemon_muerto)  # Lo retira de lista de muertos

                # Volver a la habitacion inicial
                self.current_room = 1

                # Coordenadas iniciales
                self.player_sprite.center_x = 840
                self.player_sprite.center_y = 120

                break  # Termina el combate


############## FUNCIONES NECESARIAS PARA EL COMBATE ##############

def pocion(entrenador, vida_aliado, vida_maxima):
    if vida_aliado != vida_maxima and entrenador["pocion"] != 0:
        entrenador.inventario.pop("pocion")
        return vida_aliado * 1.5

    else:
        return vida_maxima


def exp(exp_actual, lvl_aliado, lvl_enemigo):
    # Comprobador de diferencia de niveles entre aliado y enemigo
    dif_nivel = lvl_aliado - lvl_enemigo
    # si nivel aliado es mayor->dara menos exp
    # si nivel aliado es menor->dara mas exp
    # si los niveles son iguales->dara un numero base de exp
    if dif_nivel == 0:
        exp_actual = exp_actual + 8
    elif dif_nivel > 0:
        exp_actual = exp_actual + 5
    elif dif_nivel < 0:
        exp_actual = exp_actual + 13

    return exp_actual


def huir(entrenador):
    x = random.randrange(9)  # Numeros del 0 al 9

    entrenador.lista_equipo["cuerda_huida"] = entrenador.inventario["cuerda_huida"] - 1

    # La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
    if -1 < x < 3:
        return True
    else:
        return False


def atacar(tipo_aliado, tipo_enemigo, hp_enemigo, hp_total, ataque):
    if tipo_aliado == "demonio":
        if tipo_enemigo == "demonio":  # demonio vs demonio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "cometa":  # demonio vs cometa
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "volcanico":  # demonio vs volcanico
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "estelar":  # demonio vs estelar
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "vacio":  # demonio vs vacio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "lunar":  # demonio vs lunar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

    elif tipo_aliado == "cometa":
        if tipo_enemigo == "demonio":  # cometa vs demonio
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "cometa":  # cometa vs cometa
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "volcanico":  # cometa vs volcanico
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "estelar":  # cometa vs estelar
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "vacio":  # cometa vs vacio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "lunar":  # cometa vs lunar
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

    elif tipo_aliado == "volcanico":
        if tipo_enemigo == "demonio":  # volcanico vs demonio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "cometa":  # volcanico vs cometa
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "volcanico":  # volcanico vs volcanico
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "estelar":  # volcanico vs estelar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "vacio":  # volcanico vs vacio
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "lunar":  # volcanico vs lunar
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

    elif tipo_aliado == "estelar":
        if tipo_enemigo == "demonio":  # estelar vs demonio
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "cometa":  # estelar vs cometa
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "volcanico":  # estelar vs volcanico
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "estelar":  # estelar vs  estelar
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "vacio":  # estelar vs vacio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "lunar":  # estelar vs  lunar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

    elif tipo_aliado == "vacio":
        if tipo_enemigo == "demonio":  # vacio vs demonio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "cometa":  # vacio vs cometa
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "volcanico":  # vacio vs volcanico
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "estelar":  # vacio vs estelar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "vacio":  # vacio vs vacio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "lunar":  # vacio vs lunar
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

    elif tipo_aliado == "lunar":
        if tipo_enemigo == "demonio":  # lunar vs demonio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

    elif tipo_enemigo == "cometa":  # lunar vs cometa
        if hp_enemigo > hp_total - ataque * 1.5:
            return hp_enemigo - 1
        else:
            return hp_total - ataque * 1.5

    elif tipo_enemigo == "volcanico":  # lunar vs volcanico
        if hp_enemigo > hp_total - ataque:
            return hp_enemigo - 1
        else:
            return hp_total - ataque

    elif tipo_enemigo == "estelar":  # lunar vs estelar
        if hp_enemigo > hp_total - ataque * 0.5:
            return hp_enemigo - 1
        else:
            return hp_total - ataque * 0.5

    elif tipo_enemigo == "vacio":  # lunar vs vacio
        if hp_enemigo > hp_total - ataque * 1.5:
            return hp_enemigo - 1
        else:
            return hp_total - ataque * 1.5

    elif tipo_enemigo == "lunar":  # lunar vs lunar
        if hp_enemigo > hp_total - ataque:
            return hp_enemigo - 1
        else:
            return hp_total - ataque
