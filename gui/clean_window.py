import math
import random
import time

from collections import deque
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

from past.builtins import xrange  # Python3

TICKS_PER_SEC = 60

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # The label that is displayed in the top left of the canvas.
        self.label = pyglet.text.Label('', font_name='Arial', font_size=18,
            x=10, y=self.height - 10, anchor_x='left', anchor_y='top',
            color=(0, 0, 0, 255))

        # This call schedules the `update()` method to be called
        # TICKS_PER_SEC. This is the main game event loop.
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

    def update(self, x):
        pass

    def on_key_press(self, symbol, modifiers):
        """ Called when the player presses a key. See pyglet docs for key
        mappings.

        Parameters
        ----------
        symbol : int
            Number representing the key that was pressed.
        modifiers : int
            Number representing any modifying keys that were pressed.

        """
        if symbol == key.ESCAPE:
            self.set_exclusive_mouse(False)

    def set_exclusive_mouse(self, exclusive):
        """ If `exclusive` is True, the game will capture the mouse, if False
        the game will ignore the mouse.

        """
        super(Window, self).set_exclusive_mouse(exclusive)
        self.exclusive = exclusive

    def set_2d(self):
        """ Configure OpenGL to draw in 2d.

        """
        width, height = self.get_size()
        glDisable(GL_DEPTH_TEST)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_draw(self):
        """ Called by pyglet to draw the canvas.

        """
        self.clear()
        #self.set_3d()
        #glColor3d(1, 1, 1)
        #self.model.batch.draw()
        self.set_2d()
        self.draw_label()
        #self.draw_reticle()

    def draw_label(self):
        """ Draw the label in the top left of the screen.

        """
        self.label.text = '%02d (%.2f, %.2f, %.2f) %d / %d' % (
            pyglet.clock.get_fps(), 1, 2, 3,
            4, 5)
        self.label.draw()

def setup():
    """ Basic OpenGL configuration.

    """
    # Set the color of "clear", i.e. the sky, in rgba.
    glClearColor(0.5, 0.69, 1.0, 1)
    # Enable culling (not rendering) of back-facing facets -- facets that aren't
    # visible to you.
    glEnable(GL_CULL_FACE)
    # Set the texture minification/magnification function to GL_NEAREST (nearest
    # in Manhattan distance) to the specified texture coordinates. GL_NEAREST
    # "is generally faster than GL_LINEAR, but it can produce textured images
    # with sharper edges because the transition between texture elements is not
    # as smooth."
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)


def main():
    window = Window(width=800, height=600, caption='Pyglet', resizable=True)
    # Hide the mouse cursor and prevent the mouse from leaving the window.
    window.set_exclusive_mouse(True)
    setup()
    pyglet.app.run()


if __name__ == '__main__':
    main()
