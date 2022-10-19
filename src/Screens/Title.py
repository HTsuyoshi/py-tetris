import pygame
from pygame.surface import Surface

import sys

from Screens.Content import Content, State
from Options.Colors import Colors
from Options.Options import KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL
from Options.Options import TITLE_H_START, TITLE_H_SIZE, TITLE_W_START, BUTTON_H, BUTTON_W
from Options.Options import FONT

class Title(Content):
    def __init__(self) -> None:
        self.options: list[str] = [
                'Play',
                'Options',
                'Exit'
                ]
        self.border: int = (TITLE_H_SIZE - (len(self.options) * BUTTON_H)) // (2 * len(self.options))

    def update(self, display: Surface) -> State:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos: tuple[int,int] = pygame.mouse.get_pos()
                    if pos[0] > TITLE_W_START and pos[0] < TITLE_W_START + BUTTON_W:
                        start: int = TITLE_H_START
                        if pos[1] > start and pos[1] < start + BUTTON_H:
                            return State.Game
                        start += BUTTON_H + self.border
                        if pos[1] > start and pos[1] < start + BUTTON_H:
                            return State.Settings
                        start += BUTTON_H + self.border
                        if pos[1] > start and pos[1] < start + BUTTON_H:
                            pygame.quit()
                            sys.exit(0)
        pygame.key.set_repeat(KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL)
        return State.Stay

    def draw(self, display: Surface) -> None:
        self.draw_buttons(display)

    def draw_buttons(self, display) -> None:
        for i in range(len(self.options)):
            pygame.draw.rect(display,
                             Colors.GRAY.value,
                             (TITLE_W_START,
                              TITLE_H_START + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H))
            button_text: Surface = FONT.render(self.options[i], True, (255,0,0))
            display.blit(button_text, (TITLE_W_START + (BUTTON_H // 2), TITLE_H_START + (i * (BUTTON_H + self.border))))

