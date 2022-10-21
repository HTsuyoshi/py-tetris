import pygame
from pygame.surface import Surface

import sys

from Tetromino.Shape import Shape
from Screens.Content import Content, State
from Screens.Game import Game
from Options.Colors import Colors, Color_mod
from Options.Options import TITLE_H_START, TITLE_H_SIZE, TITLE_W_START, BUTTON_H, BUTTON_W
from Options.Options import TITLE_ICON_H_START, TITLE_ICON_W_START, ICON_H, ICON_W
from Options.Options import FONT, BRICK_SIZE

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
        return State.Stay

    def draw(self, display: Surface) -> None:
        self.draw_buttons(display)
        self.draw_title(display)

    def draw_buttons(self, display) -> None:
        for i in range(len(self.options)):
            pygame.draw.rect(display,
                             Colors.PURPLE.value,
                             (TITLE_W_START,
                              TITLE_H_START + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H // 2))
            pygame.draw.rect(display,
                             Color_mod().get_shadow_from_color(Colors.PURPLE),
                             (TITLE_W_START,
                              TITLE_H_START + (i * (BUTTON_H + self.border)) + (BUTTON_H // 2),
                              BUTTON_W,
                              BUTTON_H // 2))
            pygame.draw.rect(display,
                             Color_mod().get_light_from_color(Colors.PURPLE),
                             (TITLE_W_START,
                              TITLE_H_START + (i * (BUTTON_H + self.border)),
                              BUTTON_W,
                              BUTTON_H),
                             width=4)
            button_text: Surface = FONT.render(self.options[i], True, Colors.WHITE.value)
            display.blit(button_text, (TITLE_W_START + (BUTTON_H // 2), TITLE_H_START + (i * (BUTTON_H + self.border))))

    def draw_title(self, display: Surface) -> None:
        game: Game = Game()
        start_w: int = TITLE_ICON_W_START + (ICON_W // 2)  - (2 * BRICK_SIZE)
        start_h: int = TITLE_ICON_H_START + (3 * BRICK_SIZE) // 2
        colors: list[Colors] = [Colors.YELLOW, Colors.RED, Colors.PURPLE, Colors.BLUE]
        offset: int = 16

        # Triangle background
        for i in range(4):
            pygame.draw.line(display,
                             Color_mod().get_light_from_color(colors[i]),
                             (TITLE_ICON_W_START, TITLE_ICON_H_START + (i * offset)),
                             (TITLE_ICON_W_START + ICON_W, TITLE_ICON_H_START + 30 + (i * offset)),
                             width=2)

        # S Tetromino
        for i in range(2):
            for j in range(2):
                game.brick_skin.draw_brick(display,
                                           start_w + 10 + (6 * BRICK_SIZE) + (j * BRICK_SIZE) - (i * BRICK_SIZE),
                                           start_h - 60 + (i * BRICK_SIZE),
                                           BRICK_SIZE,
                                           Colors.RED.value)

        # J Tetromino
        for i in range(3):
            game.brick_skin.draw_brick(display,
                                       start_w + 10 + (3 * BRICK_SIZE),
                                       start_h - 70 - BRICK_SIZE + (i * BRICK_SIZE),
                                       BRICK_SIZE,
                                       Colors.BLUE.value)
        game.brick_skin.draw_brick(display,
                                   start_w + 10 + (2 * BRICK_SIZE),
                                   start_h - 70 - (BRICK_SIZE),
                                   BRICK_SIZE,
                                   Colors.BLUE.value)

        # L Tetromino
        for i in range(3):
            game.brick_skin.draw_brick(display,
                                       start_w,
                                       start_h - 80 - BRICK_SIZE + (i * BRICK_SIZE),
                                       BRICK_SIZE,
                                       Colors.ORANGE.value)
        game.brick_skin.draw_brick(display,
                                   start_w + BRICK_SIZE,
                                   start_h - 80 + (BRICK_SIZE),
                                   BRICK_SIZE,
                                   Colors.ORANGE.value)

        # Z Tetromino
        for i in range(2):
            for j in range(2):
                game.brick_skin.draw_brick(display,
                                           start_w + 10 - (4 * BRICK_SIZE) + (j * BRICK_SIZE) + (i * BRICK_SIZE),
                                           start_h - 90 + (i * BRICK_SIZE),
                                           BRICK_SIZE,
                                           Colors.GREEN.value)

        # I Tetromino
        for i in range(4):
            game.brick_skin.draw_brick(display,
                                       start_w - 20,
                                       start_h - 40 - (2 * BRICK_SIZE) + (i * BRICK_SIZE),
                                       BRICK_SIZE,
                                       Colors.CYAN.value)

        # O Tetromino
        for i in range(2):
            for j in range(2):
                game.brick_skin.draw_brick(display,
                                           start_w + 20 + (2 * BRICK_SIZE) + (j * BRICK_SIZE),
                                           start_h - 30 + (i * BRICK_SIZE),
                                           BRICK_SIZE,
                                           Colors.YELLOW.value)

        # T Tetromino
        for i in range(3):
            game.brick_skin.draw_brick(display,
                                       start_w + (i * BRICK_SIZE),
                                       start_h,
                                       BRICK_SIZE,
                                       Colors.PURPLE.value)
        game.brick_skin.draw_brick(display,
                                   start_w + BRICK_SIZE,
                                   start_h + BRICK_SIZE,
                                   BRICK_SIZE,
                                   Colors.PURPLE.value)
        # Triangle foreground
        for i in range(4):
            pygame.draw.lines(display,
                              Color_mod().get_light_from_color(colors[i]),
                              False,
                              [(TITLE_ICON_W_START + ICON_W, TITLE_ICON_H_START + 30 + (i * offset)),
                               (TITLE_ICON_W_START + (ICON_W// 2), TITLE_ICON_H_START + ICON_H + (i * offset)),
                               (TITLE_ICON_W_START, TITLE_ICON_H_START + (i * offset))],
                               width=2)
