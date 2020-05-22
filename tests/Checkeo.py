
#Return True: el combate continua
#Return False: el combate acaba

def checkeo(aliado, enemigo, room_anterior, x_anterior, y_anterior):

    if aliado.HP != 0 and enemigo != 0:

        #El combate continua
        return True

    elif aliado.HP == 0:

        self.jugador.lista_muertos.append(self.jugador.lista_equipo[0])  # Meter en la lista de muertos
        self.jugador.lista_equipo.pop(self.jugador.lista_equipo[0])  # Retirar del equipo de aliado

        #Intentar cambiar pokemon
        if len(self.jugador.lista_equipo) != 0:

            #Llamar cambiar pokemon
            cambiar_pokemon()
            return True

        else:

            #Pierde el combate, volver al inicio
            # Volver a la habitacion inicial
            self.current_room = 1

            # Coordenadas iniciales
            self.player_sprite.center_x = 840
            self.player_sprite.center_y = 120

            return False

    elif enemigo.HP == 0:

        #Gana el combate, ganar experienci y volver a la sala
        self.jugador.lista_equipo[0].contador_exp = exp(self.jugador.lista_equipo[0].contador_exp,
                                                      self.jugador.lista_equipo[0].nivel, enemigo.nivel)

        # Volver a la habitacion anterior
        self.current_room = room_anterior

        # Coordenadas anteriores
        self.player_sprite.center_x = x_anterior
        self.player_sprite.center_y = y_anterior

        return False
