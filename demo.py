import arcade
import os
import Objeto_Entrenador
import Objeto_Pokemon
import resources

WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN_TOP = 60
VIEWPORT_MARGIN_BOTTOM = 60
VIEWPORT_RIGHT_MARGIN = 270
VIEWPORT_LEFT_MARGIN = 270

MOVEMENT_SPEED = 5




# Juego
class MyGame(arcade.Window):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(WIDTH, HEIGHT, "Juego", fullscreen=True)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        width, height = self.get_size()

        self.set_viewport(0, width, 0, height)

        self.current_room = 0

        self.wall_list = None
        self.player_sprite = None
        self.player_list = None

        self.view_left = 0
        self.view_bottom = 0
        self.physics_engine = None

        self.current_room = 0

        # Variables globales para las teclas
        self.tienda = False
        self.cambio = False
        self.combate = False
        arcade.set_background_color(arcade.color.WHITE)
    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("resources/sprites/player/Player.png.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.jugador = Objeto_Entrenador.Entrenador("jugador")

        # Contador de habitación

        self.load_habitacion(self.current_room)

    def load_habitacion(self, current_room):
        mapa = arcade.tilemap.read_tmx(f"resources/maps/nivel{current_room}.tmx")
        self.wall_list = arcade.tilemap.process_layer(mapa, "Nivel", 0.5)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        if mapa.background_color:
            arcade.set_background_color(mapa.background_color)

    def on_draw(self):

        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

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
        self.physics_engine.update()
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
