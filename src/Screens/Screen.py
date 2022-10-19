import pygame
from pygame.surface import Surface
from pygame.time import Clock

from enum import Enum
from typing import Optional

from Options.Options import WINDOW_H, WINDOW_W
from Options.Colors import Colors
from Screens.Content import Content, State
from Screens.Title import Title
from Screens.Game import Game
from Screens.Settings import Settings

class Screen():
    def __init__(self) -> None:
        self.display: Surface = pygame.display.set_mode((WINDOW_W,WINDOW_H))
        self.fps: Clock = Clock()
        self.state: State = State.Game
        self.content: Content = Title()

        while True:
            if self.state != State.Stay:
                self.change(self.state)
                self.state = State.Stay

            self.display.fill(Colors.BLACK.value)
            self.state = self.content.update(self.display)
            self.content.draw(self.display)
            pygame.display.update()
            self.fps.tick(60)

    def change(self, state: State) -> None:
        destiny: dict[State, Optional[Content]] = {
                State.Game: Game(),
                State.Title: Title(),
                State.Settings: Settings()
                }
        self.content = destiny[state]

