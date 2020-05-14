import arcade
import os
import Objeto_Entrenador
import Objeto_Pokemon


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

class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        self.wall_list = None
        self.textura = None


def setup_room_1():
    """
    Create and return room 1.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.textura = arcade.SpriteList()

    map = arcade.tilemap.read_tmx("resources/maps/nivel0.tmx")

    carga = arcade.process_layer(map,"Nivel",1)
    wall = arcade.process_layer(map,"Muros Invisibles",1)


    room.textura = carga
    room.wall_list = wall


    return room

def setup_room_2():
    """
    Create and return room 1.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.textura = arcade.SpriteList()

    map = arcade.tilemap.read_tmx("resources/maps/nivel1.tmx")

    carga = arcade.process_layer(map,"Nivel",1)
    wall = arcade.process_layer(map,"Muros Invisibles",1)


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
        self.cura = False


    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedWalkingSprite()

        self.player_sprite.stand_right_textures = []
        self.player_sprite.stand_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der0.png"))

        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq0.png"))

        self.player_sprite.walk_right_textures = []
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der1.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der2.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der3.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der4.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der5.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der6.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der7.png"))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("resources/sprites/player/Derecha/Der8.png"))

        self.player_sprite.walk_left_textures = []
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq1.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq2.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq3.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq4.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq5.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq6.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq7.png"))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("resources/sprites/player/Izquierda/Izq8.png"))

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




        #Posición de inicio del jugador
        self.player_sprite.center_x = 85
        self.player_sprite.center_y = 537.5

        self.player_list.append(self.player_sprite)

        self.top_rooom = 1
        self.current_room = 0
        self.rooms = []

        room = setup_room_1()
        self.rooms.append(room)
        room = setup_room_2()
        self.rooms.append(room)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        self.jugador = Objeto_Entrenador.Entrenador("jugador")

    def genera_texto(self,text):

        arcade.draw_lrwh_rectangle_textured(self.view_left,self.player_sprite.center_y/5.15,WIDTH,HEIGHT/2,arcade.load_texture("resources/sprites/trainer/"+text))

    def on_draw(self):

        arcade.start_render()
        self.rooms[self.current_room].textura.draw()
        self.rooms[self.current_room].wall_list.draw()
        self.player_list.draw()

        #Cuadros de texto correspondientes al pueblo
        if(self.current_room == 0 and self.player_sprite.center_x == 471 and self.player_sprite.center_y == 681.5 ):
            self.genera_texto("cuadrado.png")
        if (self.current_room == 0 and self.player_sprite.center_x == 745 and self.player_sprite.center_y == 649.5):
            self.genera_texto("cuadrado.png")
            self.tienda == True

            
        #Mapa de coordenadas utilizado para saber la dirección
        arcade.draw_text("Coordenada x:"+ str(self.player_sprite.center_x),self.player_sprite.center_x+10,self.player_sprite.center_y, arcade.color.BLACK)
        arcade.draw_text("Coordenada y:"+str(self.player_sprite.center_y), self.player_sprite.center_x+10, self.player_sprite.center_y-10, arcade.color.BLACK)
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
        if (self.combate == True):
            if key == arcade.key.KEY_1:      pass
            if key == arcade.key.KEY_2:      pass
            if key == arcade.key.KEY_3:
                self.cambio = True
            if key == arcade.key.KEY_4:      pass

        if (self.combate == True and self.cambio == True):
            if key == arcade.key.KEY_1:      pass
            if key == arcade.key.KEY_2:      pass
            if key == arcade.key.KEY_3:      pass
            if key == arcade.key.KEY_4:      pass
            if key == arcade.key.KEY_5:      pass
            if key == arcade.key.KEY_6:      pass

        if (self.tienda == True):
            if key == arcade.key.KEY_1:
                self.jugador.restar_dinero()
                self.jugador.inventairo["Poción"] += 1
            if key == arcade.key.KEY_2:
                self.jugador.restar_dinero()
                self.jugador.inventairo["Super Poción"] += 1
            if key == arcade.key.KEY_3:
                self.jugador.restar_dinero()
                self.jugador.inventairo["Mega Poción"] += 1
            if key == arcade.key.KEY_4:
                self.jugador.restar_dinero()
                self.jugador.inventairo["Cuerda huida"] += 1

        if key == arcade.key.Q and self.jugador.inventairo["Cuerda huida"] != 0 and self.current_room != 0:
            self.jugador.inventairo["Cuerda huida"] -= 1
            self.current_room = 0

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

        #Sistema para comprobar el mayor de los pisos y cambiar al piso donde se encontraba el jugador cuando sale de la torre
        if(self.current_room>self.top_rooom and self.current_room !=10):
            self.top_rooom = self.current_room
        #Carga el piso donde se encontraba el jugador por ultima vez
        if(self.current_room == 0 and self.player_sprite.center_x == 843 and self.player_sprite.center_y == 137.5):
            self.current_room = self.top_rooom
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 165
            self.player_sprite.center_y = 465

        #Carga el piso del pueblo al salir del primer piso
        if (self.current_room == 1 and self.player_sprite.center_x == 169 and self.player_sprite.center_y == 470.5):
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 840
            self.player_sprite.center_y = 120

        #Sistema de camara para jugador
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
