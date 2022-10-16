import pygame
from pygame.surface import Surface
from pygame.font import SysFont, Font

import sys
from copy import copy

from Options import  BRICK_SIZE, GAME_H_START, GAME_W_START, GAME_H_END, GAME_W_END, WINDOW_W, WINDOW_H, NEXT_TETROMINO_H, NEXT_TETROMINO_W, TETROMINO_SHOWN, HOLD_TETROMINO_H, HOLD_TETROMINO_W, BORDER, OFFSCREEN_BRICK_SIZE, TETROMINO_SHADOW
from Tetromino import Tetromino
from Content import Content
from Colors import Colors, Color_mod
from Logic import Logic

class Game(Content):
    def __init__(self) -> None:
        self.game: Logic = Logic()
        self.border: int = BORDER
        self.brick_size: int = OFFSCREEN_BRICK_SIZE

    def update(self, display: Surface) -> None:
        self.game.input_action()
            # Put into Title()
            #for e in pygame.event.get():
            #    if e.type == pygame.QUIT:
            #        pygame.quit()
            #        sys.exit(0)
        if not self.game.check_alive():
            pygame.quit()
            sys.exit(0)

    def draw(self, display: Surface) -> None:
        self.draw_grid(display)
        self.draw_border(display)
        self.draw_score(display)
        self.draw_next_tetromino(display)
        self.draw_hold_tetromino(display)
        if TETROMINO_SHADOW: self.draw_shadow_tetromino(display)
        self.draw_current_tetromino(display)

    def draw_grid(self, display: Surface) -> None:
        for i in range(2, len(self.game.grid)):
            for j in range(len(self.game.grid[i])):
                pygame.draw.rect(display,
                                 self.game.grid[i][j],
                                 ((GAME_W_START + (j * BRICK_SIZE),
                                 GAME_H_START + (i * BRICK_SIZE),
                                 BRICK_SIZE,
                                 BRICK_SIZE)))

        for i in range(2, len(self.game.grid)):
            pygame.draw.line(display,
                             Colors.GRAY.value,
                             (GAME_W_START, GAME_H_START + i * BRICK_SIZE),
                             (GAME_W_END, GAME_H_START + i * BRICK_SIZE))

        for i in range(len(self.game.grid[0])):
            pygame.draw.line(display, Colors.GRAY.value,
                             (GAME_W_START + i * BRICK_SIZE, GAME_H_START + (2 * BRICK_SIZE)),
                             (GAME_W_START + i * BRICK_SIZE, GAME_H_END))

    def draw_border(self, display: Surface) -> None:
        pygame.draw.line(display,
                         Colors.WHITE.value,
                         (GAME_W_START, GAME_H_START + (2 * BRICK_SIZE)),
                         (GAME_W_START, GAME_H_END))
        pygame.draw.line(display,
                         Colors.WHITE.value,
                         (GAME_W_END, GAME_H_START + (2 * BRICK_SIZE)),
                         (GAME_W_END, GAME_H_END))
        pygame.draw.line(display, Colors.WHITE.value,
                         (GAME_W_START, GAME_H_START + (2 * BRICK_SIZE)),
                         (GAME_W_END, GAME_H_START + (2 * BRICK_SIZE)))
        pygame.draw.line(display,
                         Colors.WHITE.value,
                         (GAME_W_START,GAME_H_END),
                         (GAME_W_END, GAME_H_END))

    def draw_score(self, display: Surface) -> None:
        font: Font = SysFont('Source Code Variable', 30)
        score_text: Surface = font.render(f'Score: {self.game.score}', True, Colors.WHITE.value)
        display.blit(score_text, (WINDOW_W // 12, 300))

    def draw_next_tetromino(self, display: Surface) -> None:
        for i in range(TETROMINO_SHOWN):
            x: int = NEXT_TETROMINO_W
            y: int = NEXT_TETROMINO_H + (i * 4 * self.brick_size) + (i * 3 * self.border)
            pygame.draw.rect(display,
                             Colors.WHITE.value,
                             (x - self.border,
                              y - self.border,
                              (4 * self.brick_size) + 2 * self.border,
                              (4 * self.brick_size) + 2 * self.border),
                             width=1)
            self.draw_tetromino(display,
                                x,
                                y,
                                self.game.next_tetrominos[i],
                                self.brick_size)

    def draw_hold_tetromino(self, display: Surface) -> None:
        x: int = HOLD_TETROMINO_H
        y: int = HOLD_TETROMINO_W
        pygame.draw.rect(display,
                         Colors.WHITE.value,
                         (x - self.border,
                          y - self.border,
                          (4 * self.brick_size) + 2 * self.border,
                          (4 * self.brick_size) + 2 * self.border),
                         width=1)
        if self.game.hold_tetromino:
            self.draw_tetromino(display,
                                x,
                                y,
                                self.game.hold_tetromino,
                                self.brick_size)

    def draw_current_tetromino(self, display: Surface) -> None:
        if not self.game.current_tetromino: return

        x = GAME_W_START + (self.game.current_tetromino.x * BRICK_SIZE)
        y = GAME_H_START + (self.game.current_tetromino.y * BRICK_SIZE)
        self.draw_tetromino(display, x, y, self.game.current_tetromino)

    def draw_shadow_tetromino(self, display: Surface):
        if not self.game.current_tetromino: return

        shadow_tetromino: Tetromino = copy(self.game.current_tetromino)
        shadow_tetromino.hard_drop(self.game.grid)
        shadow_tetromino.color = Color_mod().get_shadow[shadow_tetromino.color]
        x = GAME_W_START + (shadow_tetromino.x * BRICK_SIZE)
        y = GAME_H_START + (shadow_tetromino.y * BRICK_SIZE)
        self.draw_tetromino(display, x, y, shadow_tetromino)

    def draw_tetromino(self, display: Surface, x_offset: int, y_offset: int, tetromino: Tetromino, brick_size: int = BRICK_SIZE):
        for i in range(4):
            for j in range(4):
                if tetromino.get_shape()[i][j] == ' ':
                    continue

                x = x_offset + (j * brick_size)
                y = y_offset + (i * brick_size)

                pygame.draw.rect(display,
                                 tetromino.color.value,
                                 (x, y,
                                 brick_size,
                                 brick_size))

