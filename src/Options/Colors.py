from enum import Enum

from Tetromino.Shape import Shape

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

    def get_shadow_from_color(self, color: Colors) -> tuple[int,int,int]:
        return (color.value[0] // 2, color.value[1] // 2, color.value[2] // 2)

    def get_shadow_from_tuple(self, color: tuple[int,int,int]) -> tuple[int,int,int]:
        return (color[0] // 2, color[1] // 2, color[2] // 2)
