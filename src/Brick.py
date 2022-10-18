import pygame
from pygame.surface import Surface

import abc
from enum import Enum
from Colors import Colors, Color_mod

class Brick(abc.ABC):
    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   grid: list[list[tuple[int, int, int]]]) -> None:
        pass

class Standard_brick(Brick):
    def __init__(self):
        self.border = 1

    def draw_brick(self,
                   display: Surface,
                   x: int,
                   y: int,
                   brick_size: int,
                   brick_color: tuple[int, int, int],
                   grid: list[list[tuple[int, int, int]]]) -> None:
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
                         brick_size - self.border,
                         brick_size - self.border),
                         width=2)
