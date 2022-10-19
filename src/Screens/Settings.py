import pygame
from pygame.surface import Surface

import sys
from enum import Enum

from Screens.Content import Content, State
from Options.Options import KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL

class Settings(Content):
    def __init__(self) -> None:
        self.font: pygame.font.Font = pygame.font.SysFont('Source Code Variable', 30)
        self.score_text: Surface = self.font.render('Score', True, (255,0,0))
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

