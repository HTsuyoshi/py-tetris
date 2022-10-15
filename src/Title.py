import pygame
from pygame.surface import Surface

from Content import Content

class Title(Content):
    def __init__(self) -> None:
        self.font: pygame.font.Font = pygame.font.SysFont('Source Code Variable', 30)
        self.score_text = self.font.render('Score', True, (255,0,0))

    def update(self, display: Surface) -> None:
        pass

    def draw(self, display: Surface) -> None:
        pass

