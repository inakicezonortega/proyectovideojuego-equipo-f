import arcade
import os

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = ""

START = 0
END = 2000
STEP = 50

VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):
        """
        Constructor
        """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True, resizable=True)

        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_resize(self, width, height):
        """ Reescala la pantalla automaticamente """
        super().on_resize(width, height)

    def on_draw(self):
        """
        Carga la pantalla
        """
        arcade.start_render()

        left, screen_width, bottom, screen_height = self.get_viewport()

        text_size = 18
        arcade.draw_text("Pulsa F para cambiar el tipo de pantalla.",
                         screen_width // 2, screen_height // 2 - 20,
                         arcade.color.WHITE, text_size, anchor_x="center")


    def on_key_press(self, key, modifiers):

        if key == arcade.key.F:

            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)


def main():

    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()