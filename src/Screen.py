import pygame, sys
from pygame.surface import Surface
from pygame.time import Clock
from enum import Enum

from Options import WINDOW_H, WINDOW_W
from Content import Content
from Title import Title
from Game import Game
from Colors import Colors

class State(Enum):
    Stay = -1
    Title = 0
    Game = 1

class Screen():
    def __init__(self) -> None:
        self.display: Surface = pygame.display.set_mode((WINDOW_W,WINDOW_H))
        self.fps: Clock = Clock()
        self.state: State = State.Game
        self.content: Content

        while True:
            if self.state == State.Title:
                self.content = Title()
                self.state = State.Stay
            elif self.state == State.Game:
                self.content = Game()
                self.state = State.Stay

            self.display.fill(Colors.BLACK.value)
            self.content.update(self.display)
            self.content.draw(self.display)
            pygame.display.update()
            self.fps.tick(60)


