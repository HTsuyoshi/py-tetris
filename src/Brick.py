import pygame
from pygame.surface import Surface

import abc
from Colors import Colors, Color_mod

class Brick(abc.ABC):
    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   shadow: bool = False) -> None:
        pass

class Standard_brick(Brick):
    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   shadow: bool = False) -> None:
        pygame.draw.rect(display,
                         brick_color,
                         (x,
                         y,
                         brick_size,
                         brick_size))

class Line_brick(Brick):
    def __init__(self):
        self.offset: int = 4

    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   shadow: bool = False) -> None:
        pygame.draw.rect(display,
                         brick_color,
                         (x,
                         y,
                         brick_size - self.offset,
                         brick_size - self.offset))
        pygame.draw.rect(display,
                         Color_mod().get_shadow_from_tuple(brick_color),
                         (x + self.offset,
                         y + self.offset,
                         brick_size - self.offset,
                         brick_size - self.offset),
                         width=2)

class Shiny_brick(Brick):
    def __init__(self):
        self.border: int = 2

    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   shadow: bool = False) -> None:
        pygame.draw.rect(display,
                         brick_color,
                         (x,
                         y,
                         brick_size,
                         brick_size))
        pygame.draw.rect(display,
                         Color_mod().get_shadow_from_tuple(brick_color),
                         (x + self.border,
                         y + self.border,
                         brick_size - (2 * self.border),
                         brick_size - (2 * self.border)),
                         width=4)
        pygame.draw.rect(display,
                         Colors.GRAY.value if shadow else Colors.WHITE.value,
                         (x + 6,
                         y + 6,
                         brick_size // 4,
                         1),
                         width=2)

class Open_brick(Brick):
    def __init__(self):
        self.border: int = 4

    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   shadow: bool = False) -> None:
        pygame.draw.rect(display,
                         brick_color,
                         (x,
                         y,
                         brick_size,
                         brick_size),
                         width=4)
        pygame.draw.rect(display,
                         Color_mod().get_shadow_from_tuple(brick_color),
                         (x + self.border,
                         y + self.border,
                         brick_size - (2 * self.border),
                         brick_size - (2 * self.border)),
                         width=4)

class Border_brick(Brick):
    def __init__(self):
        self.border: int = 12

    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   shadow: bool = False) -> None:
        pygame.draw.rect(display,
                         brick_color,
                         (x,
                         y,
                         brick_size,
                         brick_size),
                         width=4)
        pygame.draw.rect(display,
                         brick_color,
                         (x + self.border,
                         y + self.border,
                         brick_size - (2 * self.border),
                         brick_size - (2 * self.border)))
