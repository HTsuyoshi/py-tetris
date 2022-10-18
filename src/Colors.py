from enum import Enum

from Shape import Shape

class Colors(Enum):
    BLACK = (0,0,0)
    GRAY = (128,128,128)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    CYAN = (0,255,255)
    YELLOW = (255,255,0)
    PURPLE = (127,0,127)
    ORANGE = (255,127,0)
    SHADOW_RED = (127,0,0)
    SHADOW_GREEN = (0,127,0)
    SHADOW_BLUE = (0,0,127)
    SHADOW_CYAN = (0,127,127)
    SHADOW_YELLOW = (127,127,0)
    SHADOW_PURPLE = (63,0,63)
    SHADOW_ORANGE = (127,63,0)

class Color_mod:
    def __init__(self):
        self.get_color = {
                Shape.SHAPE_S: Colors.GREEN,
                Shape.SHAPE_Z: Colors.RED,
                Shape.SHAPE_J: Colors.BLUE,
                Shape.SHAPE_L: Colors.ORANGE,
                Shape.SHAPE_I: Colors.CYAN,
                Shape.SHAPE_T: Colors.PURPLE,
                Shape.SHAPE_O: Colors.YELLOW
                }
        self.get_shadow = {
                Colors.GREEN: Colors.SHADOW_GREEN,
                Colors.RED: Colors.SHADOW_RED,
                Colors.BLUE: Colors.SHADOW_BLUE,
                Colors.ORANGE: Colors.SHADOW_ORANGE,
                Colors.CYAN: Colors.SHADOW_CYAN,
                Colors.PURPLE: Colors.SHADOW_PURPLE,
                Colors.YELLOW: Colors.SHADOW_YELLOW,
                Colors.SHADOW_GREEN: Colors.SHADOW_GREEN,
                Colors.SHADOW_RED: Colors.SHADOW_RED,
                Colors.SHADOW_BLUE: Colors.SHADOW_BLUE,
                Colors.SHADOW_ORANGE: Colors.SHADOW_ORANGE,
                Colors.SHADOW_CYAN: Colors.SHADOW_CYAN,
                Colors.SHADOW_PURPLE: Colors.SHADOW_PURPLE,
                Colors.SHADOW_YELLOW: Colors.SHADOW_YELLOW
                }
