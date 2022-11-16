import pygame
from pygame.surface import Surface

import sys

from Screens.Content import Content, State
from Options.Options import KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL, TITLE_H_START, TITLE_W_START, TITLE_H_SIZE, BUTTON_H, BUTTON_W, FONT, BRICK_SIZE, ICON_H, ICON_W
from Options.Colors import Colors, Color_mod

class Settings(Content):
    def __init__(self) -> None:
        self.options_1: list[str] = [
                'Next tetr',
                'Tetr. shadow',
                'Fps',
                'Fall Speed',
                'LockDelay'
                ]
        self.options_2: list[str] = [
                'Key Rep. Interval',
                'Key Rep. Delay',
                'Soft Drop',
                'Return'
                ]
        self.border: int = (TITLE_H_SIZE - (len(self.options_1) * BUTTON_H)) // (2 * len(self.options_1))

    def update(self, display: Surface) -> State:
        # Remover e colocar em opcoes no Title()
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                return State.Title
        pygame.key.set_repeat(KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL)
        return State.Stay

    def draw(self, display: Surface) -> None:
        self.draw_buttons(display)

    def draw_buttons(self, display) -> None:
        for i in range(len(self.options_1)):
            pygame.draw.rect(display,
                             Colors.PURPLE.value,
                             (TITLE_W_START - (3 * BUTTON_W // 4),
                              TITLE_H_START // 2 + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H // 2))
            pygame.draw.rect(display,
                             Color_mod().get_shadow_from_color(Colors.PURPLE),
                             (TITLE_W_START - (3 * BUTTON_W // 4),
                              TITLE_H_START // 2 + (i * (BUTTON_H + self.border)) + (BUTTON_H // 2),
                              BUTTON_W,
                              BUTTON_H // 2))
            pygame.draw.rect(display,
                             Color_mod().get_light_from_color(Colors.PURPLE),
                             (TITLE_W_START - (3 * BUTTON_W // 4),
                              TITLE_H_START // 2 + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H),
                             width=4)
            button_text: Surface = FONT.render(self.options_1[i], True, Colors.WHITE.value)
            display.blit(button_text, (TITLE_W_START - (3 * BUTTON_W // 4) + (BUTTON_H // 2), TITLE_H_START // 2 + (i * (BUTTON_H + self.border))))
        for i in range(len(self.options_2)):
            pygame.draw.rect(display,
                             Colors.PURPLE.value,
                             (TITLE_W_START + (3 * BUTTON_W // 4),
                              TITLE_H_START // 2 + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H // 2))
            pygame.draw.rect(display,
                             Color_mod().get_shadow_from_color(Colors.PURPLE),
                             (TITLE_W_START + (3 * BUTTON_W // 4),
                              TITLE_H_START // 2 + (i * (BUTTON_H + self.border)) + (BUTTON_H // 2),
                              BUTTON_W,
                              BUTTON_H // 2))
            pygame.draw.rect(display,
                             Color_mod().get_light_from_color(Colors.PURPLE),
                             (TITLE_W_START + (3 * BUTTON_W // 4),
                              TITLE_H_START // 2 + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H),
                             width=4)
            button_text: Surface = FONT.render(self.options_2[i], True, Colors.WHITE.value)
            display.blit(button_text, (TITLE_W_START + (3 * BUTTON_W // 4) + (BUTTON_H // 2), TITLE_H_START // 2 + (i * (BUTTON_H + self.border))))
