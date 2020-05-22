import random
def atacar(atacante , defensor):

    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                 defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "cometa":  # demonio vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "volcanico":  # demonio vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "estelar":  # demonio vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "vacio":  # demonio vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "lunar":  # demonio vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

    elif atacante.tipo == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "cometa":  # cometa vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "volcanico":  # cometa vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "estelar":  # cometa vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "vacio":  # cometa vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "lunar":  # cometa vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

    elif atacante.tipo == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "cometa":  # volcanico vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "estelar":  # volcanico vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "vacio":  # volcanico vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "lunar":  # volcanico vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

    elif atacante.tipo == "estelar":
        if defensor.tipo == "demonio":  # estelar vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "cometa":  # estelar vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "estelar":  # estelar vs  estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "vacio":  # estelar vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "lunar":  # estelar vs  lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

    elif atacante.tipo == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "cometa":  # vacio vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "estelar":  # vacio vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "vacio":  # vacio vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "lunar":  # vacio vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

    elif atacante.tipo == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

    elif defensor.tipo == "cometa":  # lunar vs cometa
        if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque * 1.5

    elif defensor.tipo == "volcanico":  # lunar vs volcanico
        if defensor.HP > defensor.HP_MAX - atacante.ataque:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque

    elif defensor.tipo == "estelar":  # lunar vs estelar
        if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque * 0.5

    elif defensor.tipo == "vacio":  # lunar vs vacio
        if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque * 1.5

    elif defensor.tipo == "lunar":  # lunar vs lunar
        if defensor.HP > defensor.HP_MAX - atacante.ataque:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque
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

def huir():
    x = random.randrange(9)  # Numeros del 0 al 9

    self.jugador.lista_equipo["Cuerda Huida"] -= 1

    # La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
    if -1 < x < 3:
        return True
    else:   False

def checkeo(aliado, enemigo, room_anterior, x_anterior, y_anterior):
    if aliado.HP > 0 and enemigo.HP > 0:
        print("Todo bien")
        # El combate continua


    elif aliado.HP <= 0:
        print("Todo mal")
        self.jugador.lista_muertos.append(self.jugador.lista_equipo[0])  # Meter en la lista de muertos
        self.jugador.lista_equipo.pop(self.jugador.lista_equipo[0])  # Retirar del equipo de aliado

        # Intentar cambiar pokemon
        if len(self.jugador.lista_equipo) == 0:

            # Pierde el combate, volver al inicio
            # Volver a la habitacion inicial
            self.current_room = 1

            # Coordenadas iniciales
            self.player_sprite.center_x = 840
            self.player_sprite.center_y = 120



    elif enemigo.HP <= 0:
        print("Has ganado")
        """""# Gana el combate, ganar experienci y volver a la sala
        self.jugador.lista_equipo[0].contador_exp = exp(self.jugador.lista_equipo[0].contador_exp,
                                                        self.jugador.lista_equipo[0].nivel, enemigo.nivel)

        # Volver a la habitacion anterior
        self.current_room = room_anterior

        # Coordenadas anteriores
        self.player_sprite.center_x = x_anterior
        self.player_sprite.center_y = y_anterior"""

