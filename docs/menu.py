
import arcade
import os

WIDTH = 800
HEIGHT = 600


# Mostar menu
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


# Mostrar instrucciones
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
        ##Mostrar el juego
        arcade.close_window()
        MyGame()
        arcade.run()





# Juego
class MyGame(arcade.Window):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(WIDTH, HEIGHT, "Juego", fullscreen=True)

        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Carga la pantalla del juego
        """

        arcade.start_render()
        arcade.draw_text("Juego", self.width // 2, self.height // 2 -20, arcade.color.WHITE, 20, anchor_x="center")


    def on_key_press(self, key, modifiers):

        if key == arcade.key.F:

            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)



def main():
    window = arcade.Window(WIDTH, HEIGHT, "Juego")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()



main()