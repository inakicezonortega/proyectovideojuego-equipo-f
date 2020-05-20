import arcade
import os
import Objeto_Entrenador
import Objeto_Pokemon
import random
from tests.Cambiar_Pokemon import cambiar_pokemon

WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN_TOP = 60
VIEWPORT_MARGIN_BOTTOM = 60
VIEWPORT_RIGHT_MARGIN = 270
VIEWPORT_LEFT_MARGIN = 270

MOVEMENT_SPEED = 3

#La clase room es aquella clase que crea los escenarios donde se desplaza el jugador
class Room:
    """
    Esta clase crea y caga las distintas habitaciones del juego
    """

    def __init__(self):
        self.wall_list = None
        self.textura = None


def setup_pueblo():
    """
    Crea la habitación del pueblo
    """
    room = Room()

   # Lista de Sprites
    room.wall_list = arcade.SpriteList()
    room.textura = arcade.SpriteList()

    map = arcade.tilemap.read_tmx("resources/maps/nivel0.tmx")

    carga = arcade.process_layer(map, "Nivel", 1)
    wall = arcade.process_layer(map, "Muros Invisibles", 1)

    room.textura = carga
    room.wall_list = wall

    return room


def setup_room_1():
    """
    Crea la habitacion 1.
    """
    room = Room()

    #Lista de Sprites
    room.wall_list = arcade.SpriteList()
    room.textura = arcade.SpriteList()

    map = arcade.tilemap.read_tmx("resources/maps/nivel1.tmx")

    carga = arcade.process_layer(map, "Nivel", 1)
    wall = arcade.process_layer(map, "Muros Invisibles", 1)

    room.textura = carga
    room.wall_list = wall

    return room


def setup_combate():
    """
    Create la habitación donde ocurriran los combates
    """
    room = Room()


    #Lista de Sprites
    room.wall_list = arcade.SpriteList()
    room.textura = arcade.SpriteList()

    map = arcade.tilemap.read_tmx("resources/maps/combate.tmx")

    carga = arcade.process_layer(map, "Nivel", 1)
    wall = arcade.process_layer(map, "Muros Invisibles", 1)

    room.textura = carga
    room.wall_list = wall

    return room


# Juego
class MyGame(arcade.Window):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(WIDTH, HEIGHT, "Juego", fullscreen=True)

        self.set_mouse_visible(False)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        width, height = self.get_size()

        self.set_viewport(0, width, 0, height)

        self.current_room = 0
        self.rooms = None

        self.textura = None
        self.wall_list = None
        self.player_sprite = None
        self.player_list = None

        self.view_left = 0
        self.view_bottom = 0
        self.physics_engine = None

        # Variables globales para las teclas
        self.tienda = False
        self.cambio = False
        self.combate = False
        self.cuerda_huida = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedWalkingSprite()

        self.player_sprite.stand_right_textures = []
        self.player_sprite.stand_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der0.png"))

        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(
            arcade.load_texture("resources/sprites/player/Izquierda/Izq0.png"))

        #Cargamos las texturas para el movimiento derecho
        self.player_sprite.walk_right_textures = []
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der1.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der2.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der3.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der4.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der5.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der6.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der7.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der8.png"))

        # Cargamos las texturas para el movimiento  izquierdo
        self.player_sprite.walk_left_textures = []
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq1.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq2.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq3.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq4.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq5.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq6.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq7.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq8.png"))

        # Cargamos las texturas para el movimiento abajo
        self.player_sprite.walk_down_textures = []
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj0.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj1.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj2.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj3.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj4.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj5.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj6.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj7.png"))
        self.player_sprite.walk_down_textures.append(arcade.load_texture("resources/sprites/player/Abajo/Abj8.png"))

        # Cargamos las texturas para el movimiento de arriba
        self.player_sprite.walk_up_textures = []
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr0.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr1.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr2.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr3.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr4.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr5.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr6.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr7.png"))
        self.player_sprite.walk_up_textures.append(arcade.load_texture("resources/sprites/player/Arriba/Arr8.png"))

        # Posición de inicio del jugador
        self.player_sprite.center_x = 85
        self.player_sprite.center_y = 537.5

        self.player_list.append(self.player_sprite)

        self.top_rooom = 1
        self.current_room = 0
        self.rooms = []

        room = setup_pueblo()
        self.rooms.append(room)
        room = setup_room_1()
        self.rooms.append(room)
        room = setup_combate()
        self.rooms.append(room)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        self.jugador = Objeto_Entrenador.Entrenador("jugador")


    #Esta funcion recibe el texto dentro de los sprites y dibuja el cuadro de texto
    def genera_texto(self, text):

        arcade.draw_lrwh_rectangle_textured(self.view_left, self.player_sprite.center_y / 5.15, WIDTH, HEIGHT / 2,
                                            arcade.load_texture("resources/sprites/trainer/" + text))

    def on_draw(self):

        arcade.start_render()
        self.rooms[self.current_room].textura.draw()
        self.rooms[self.current_room].wall_list.draw()
        self.player_list.draw()

        # Cuadros de texto correspondientes al pueblo
        if (self.current_room == 0 and self.player_sprite.center_x == 471 and self.player_sprite.center_y == 681.5):
            self.genera_texto("cuadrado.png")
        if (self.current_room == 0 and self.player_sprite.center_x == 745 and self.player_sprite.center_y == 649.5):
            self.genera_texto("cuadrado.png")


        arcade.draw_text("Nombre Pokemon1 + LVL", 534, 253, arcade.color.BLACK, 12)
        arcade.draw_text("HP Pokemon1", 534, 223, arcade.color.BLACK, 12)
        arcade.draw_text("Nombre Pokemon1", 300, 530, arcade.color.BLACK, 12)
        arcade.draw_text("HP Pokemon2", 300, 510, arcade.color.BLACK, 12)

        # Mapa de coordenadas utilizado para saber la dirección
        arcade.draw_text("Coordenada x:" + str(self.player_sprite.center_x), self.player_sprite.center_x + 10,
                         self.player_sprite.center_y, arcade.color.WHITE)
        arcade.draw_text("Coordenada y:" + str(self.player_sprite.center_y), self.player_sprite.center_x + 10,
                         self.player_sprite.center_y - 10, arcade.color.WHITE)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        if key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        if key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        #ERROR
        if (self.combate == True):
            if key == arcade.key.KEY_1:      pass
            if key == arcade.key.KEY_2:      pass
            if key == arcade.key.KEY_3:
                self.cambio = True
            if key == arcade.key.KEY_4:      pass
        #ERROR
        if (self.combate == True and self.cambio == True):
            if key == arcade.key.KEY_1:
                cambiar_pokemon(self.jugador, 1)
                self.cambio = False
            if key == arcade.key.KEY_2:
                cambiar_pokemon(self.jugador, 2)
                self.cambio = False
            if key == arcade.key.KEY_3:
                cambiar_pokemon(self.jugador, 3)
                self.cambio = False
            if key == arcade.key.KEY_4:
                cambiar_pokemon(self.jugador, 4)
                self.cambio = False
        #ERROR??
        if (self.tienda == True):
            if key == arcade.key.KEY_1:
                self.jugador.restar_dinero()
                self.jugador.inventario["Poción"] += 1
            if key == arcade.key.KEY_2:
                self.jugador.restar_dinero()
                self.jugador.inventario["Cuerda huida"] += 1

        if key == arcade.key.Q and self.current_room !=0 and self.jugador.inventario["Cuerda Huida"]!=0:
            self.cuerda_huida = True


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0



    def on_update(self, delta_time):
        # Call update on all sprites (The sprites don't do much in this example though.)
        self.player_list.update()
        self.player_list.update_animation()
        self.physics_engine.update()

        # Sistema para comprobar el mayor de los pisos y cambiar al piso donde se encontraba el jugador cuando sale de la torre
        if (self.current_room > self.top_rooom and self.current_room != 10):
            self.top_rooom = self.current_room
        # Carga el piso donde se encontraba el jugador por ultima vez
        if (self.current_room == 0 and self.player_sprite.center_x == 843 and self.player_sprite.center_y == 137.5):
            self.current_room = self.top_rooom
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 165
            self.player_sprite.center_y = 465

        # Carga el piso del pueblo al salir del primer piso
        if (self.current_room == 1 and self.player_sprite.center_x == 169 and self.player_sprite.center_y == 470.5):
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 840
            self.player_sprite.center_y = 120

        # Prueba combate
        if (self.current_room == 1 and self.player_sprite.center_x == 873 and self.player_sprite.center_y == 425.5):
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 300
            self.player_sprite.center_y = 55
            arcade.draw_text("Nombre Pokemon1 + LVL", 534, 253, arcade.color.BLACK, 12)
            arcade.draw_text("HP Pokemon1", 534, 223, arcade.color.BLACK, 12)
            arcade.draw_text("Nombre Pokemon1", 300, 550, arcade.color.BLACK, 12)
            arcade.draw_text("HP Pokemon2", 300, 521.5, arcade.color.BLACK, 12)
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 55

        #Sistema para regresar al pueblo con cuerda huida
        if(self.cuerda_huida ):
            self.jugador.inventario["Cuerda Huida"] -= 1
            self.cuerda_huida = False
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 70
            self.player_sprite.center_y = 537.5

        ############## TURNO VS POKEMON ##############

        def turno_aliado(, pokemon, accion):
            while True:

                # # CAMBIAR # #
                if accion == 3:
                    cambio = True
                    while not cambio:
                        num = 0
                        num += 1


                # # POCION # #
                elif accion == 2:
                    self.jugador.lista_equipo[0].HP = pocion( self.jugador.lista_equipo[0].HP,
                                                              self.jugador.lista_equipo[0].HP_MAX)


                # # CUERDA HUIDA # #
                elif accion == 4:

                    # Si tiene en el inventario
                    if  self.jugador.inventario["Cuerda Huida"] > 0:

                        # Si consigue huir
                        if huir():
                            return True  # Salir del bucle


                # #  ATACAR # #
                elif accion == 1:

                    pokemon.HP = atacar( self.jugador.lista_equipo[0].tipo, pokemon.tipo, pokemon.HP, pokemon.HP_MAX,
                                         self.jugador.lista_equipo[0].ataque)
                    return False  # Salir del bucle

        ############## TURNO VS ENTRENADOR ##############

        def turno_aliado(entrenador, rival, accion):
            while True:

                # # CAMBIAR # #
                if accion == 3:
                    cambio = True
                    while not cambio:
                        num = 0
                        num += 1


                # # POCION # #
                elif accion == 2:
                    entrenador.lista_equipo[0].HP = pocion(entrenador.lista_equipo[0].HP,entrenador.lista_equipo[0].HP_MAX)


                # # CUERDA HUIDA # #
                elif accion == 4:

                    # Si tiene en el inventario
                    if entrenador.inventario["Cuerda Huida"] > 0:

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

        def combate(entrenador, pokemon, accion, room_anterior, x_anterior, y_anterior):
            # Bucle principal
            while self.combate:

                # Ataque enemigo
                if pokemon.HP != 0:
                    entrenador.lista_equipo[0].HP = atacar(pokemon.tipo, entrenador.lista_equipo[0].tipo,
                                                           entrenador.lista_equipo[0].HP,
                                                           entrenador.lista_equipo[0].HP_MAX,
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

                    if turno_aliado(entrenador, pokemon, accion):

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

                        turno_aliado(entrenador, pokemon, accion)

                    # No quedan aliados vivos
                    else:

                        # Volver a la habitacion inicial
                        self.current_room = 1

                        # Coordenadas iniciales
                        self.player_sprite.center_x = 840
                        self.player_sprite.center_y = 120

                        break

        ############## COMBATE VS ENTRENADOR ##############

        def combate(rival, accion, room_anterior, x_anterior, y_anterior):
            # Bucle principal
            while self.combate:

                # Ataque enemigo
                if rival.lista_equipo[0].HP != 0:
                    self.jugador.lista_equipo[0].HP = atacar(rival.lista_equipo[0].tipo, self.jugador.lista_equipo[0].tipo,
                                                           self.jugador.lista_equipo[0].HP,
                                                           self.jugador.lista_equipo[0].HP_MAX,
                                                           rival.lista_equipo[0].ataque)

                # Ganar el combate
                elif rival.lista_equipo[0].HP == 0:

                    # Si quedan enemigos vivos, cambiar el que combate
                    if len(rival.lista_equipo[0] != 0):
                        rival.lista_muertos.append(rival.lista_equipo[0])  # Añado a la lista de muertos
                        rival.lista_equipo.pop(0)  # Retirara de disponibles


                    # No quedan enemigos vivos
                    else:
                        self.jugador.lista_equipo[0].contador_exp = exp(self.jugador.lista_equipo[0].contador_exp,
                                                                      self.jugador.lista_equipo[0].nivel,
                                                                      rival.lista_equipo[0].nivel)
                        # Volver a la habitacion anterior
                        self.current_room = room_anterior
                        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                         self.rooms[self.current_room].wall_list)
                        # Coordenadas anteriores
                        self.player_sprite.center_x = x_anterior
                        self.player_sprite.center_y = y_anterior
                        break

                # Si el aliado sigue con vida
                if self.jugador.lista_equipo[0].HP != 0:

                    if turno_aliado(self.jugador, rival, accion):
                        break  # Si ha huido
                    else:
                        continue  # Si no ha huido


                # Si el aliado no sigue con vida
                elif self.jugador.lista_equipo[0].HP == 0:

                    # Retirar al pokemon
                    self.jugador.lista_muertos.append(self.jugador.lista_equipo[0])  # Meter en la lista de muertos
                    self.jugador.lista_equipo.pop(self.jugador.lista_equipo[0])  # Retirar del equipo de aliado

                    # Si quedan aliados vivos
                    if len(self.jugador.lista_equipo[0] != 0):

                        turno_aliado(self.jugador, rival, accion)

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

        def pocion(vida_aliado, vida_maxima):
            if vida_aliado != vida_maxima and self.jugador.inventario["Pocion"] != 0:
                self.jugador.inventario.pop("Pocion")
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

        def huir():
            x = random.randrange(9)  # Numeros del 0 al 9

            self.jugador.lista_equipo["Cuerda Huida"] -= 1

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

        # Sistema de camara para jugador
        changed = False
        # Scroll left
        left_bndry = self.view_left + VIEWPORT_LEFT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + WIDTH - VIEWPORT_RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + HEIGHT - VIEWPORT_MARGIN_TOP
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN_BOTTOM
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            self.view_left = int(self.view_left)
            self.view_bottom = int(self.view_bottom)
            arcade.set_viewport(self.view_left,
                                WIDTH + self.view_left,
                                self.view_bottom,
                                HEIGHT + self.view_bottom)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()
