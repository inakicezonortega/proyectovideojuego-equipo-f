import arcade

WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)


MOVEMENT_SPEED = 5

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Titulo Juego", WIDTH/2, HEIGHT/2, arcade.color.RED, font_size=50, anchor_x="center")
        arcade.draw_text("Haz click para avanzar", WIDTH/2, HEIGHT/2-75, arcade.color.RED, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Opciones", WIDTH / 2, HEIGHT / 2, arcade.color.RED, font_size=50, anchor_x="center")
        arcade.draw_text("Dentro del juego, pulsa F para pantalla completa", WIDTH / 2, HEIGHT / 2- 75, arcade.color.RED, font_size=20, anchor_x="center")
        arcade.draw_text("Click para iniciar el juego", WIDTH / 2, HEIGHT / 2 - 100,
                         arcade.color.RED, font_size=15, anchor_x="center")
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = HistoriaView()
        self.window.show_view(instructions_view)


class HistoriaView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Insertar Historia Aqui", WIDTH / 2, HEIGHT / 2, arcade.color.RED, font_size=50, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        ##Mostrar el juego
        arcade.close_window()
        MyGame()
        arcade.run()


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None
def setup_pueblo():
    room=Room()

    room.wall_list = arcade.SpriteList()
    for y in (0, HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Sprites/Habitaciones/Muro_Invisible.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("Sprites/Habitaciones/Muro_Invisible.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background= arcade.load_texture("Sprites/Habitaciones/Pueblo.jpg")



# Juego
class MyGame(arcade.Window):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(WIDTH, HEIGHT, "Juego", fullscreen=True)

        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)

        self.current_room = 0

        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("Sprites/Jugador/Jugador.jpg", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Listado de habitaciones
        self.rooms = []
        self.rooms.append(setup_pueblo())

        #Contador de habitación
        self.current_room = 0

        #Fisicas
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)


    def on_draw(self):

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,WIDTH,HEIGHT,self.rooms[self.current_room].background)
        self.rooms[self.current_room].wall_list.draw()
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

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


    def on_update(self, delta_time):
        # Call update on all sprites (The sprites don't do much in this example though.)
        self.physics_engine.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.rooms[self.current_room].wall_list)

            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = WIDTH


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Juego")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()



main()