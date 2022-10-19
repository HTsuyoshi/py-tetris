import pygame
from pygame.surface import Surface

from Screens.Content import Content, State

class Settings(Content):
    def __init__(self) -> None:
        pass

    def update(self, display: Surface) -> State:
        return State.Game
        pass

    def draw(self, display: Surface) -> None:
        pass

