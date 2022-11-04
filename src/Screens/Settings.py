import pygame
from pygame.surface import Surface

import sys

from Screens.Content import Content, State
from Options.Options import KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL

class Settings(Content):
    def __init__(self) -> None:
        self.options: list[str] = [
                'Play',
                'Options',
                'Exit'
                ]

    def update(self, display: Surface) -> State:
        # Remover e colocar em opcoes no Title()
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit(0)
        pygame.key.set_repeat(KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL)
        return State.Stay

    def draw(self, display: Surface) -> None:
        pass

