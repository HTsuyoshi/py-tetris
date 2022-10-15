import pygame
from pygame.surface import Surface
from pygame.font import SysFont, Font

from Options import  BRICK_SIZE, GAME_H_START, GAME_W_START, GAME_H_END, GAME_W_END, WINDOW_W, WINDOW_H, NEXT_TETROMINO_H_START, NEXT_TETROMINO_H_END, NEXT_TETROMINO_W_END, NEXT_TETROMINO_W_START
from Tetromino import Tetromino
from Content import Content
from Colors import Colors
from Logic import Logic

class Game(Content):
    def __init__(self) -> None:
        self.game: Logic = Logic()

    def update(self, display: Surface) -> None:
        self.game.input_action()

    def draw(self, display: Surface) -> None:
        self.draw_grid(display)
        self.draw_border(display)
        self.draw_score(display)
        self.draw_next_tetromino(display)
        self.draw_current_tetromino(display)


    def draw_grid(self, display: Surface) -> None:
        for i in range(len(self.game.grid)):
            pygame.draw.line(display, Colors.GRAY.value, (GAME_W_START, GAME_H_START + i * BRICK_SIZE), (GAME_W_END, GAME_H_START + i * BRICK_SIZE))

        for i in range(len(self.game.grid[0])):
            pygame.draw.line(display, Colors.GRAY.value, (GAME_W_START + i * BRICK_SIZE, GAME_H_START), (GAME_W_START + i * BRICK_SIZE, GAME_H_END))

    def draw_border(self, display: Surface) -> None:
        pygame.draw.line(display, Colors.WHITE.value, (GAME_W_START, GAME_H_START), (GAME_W_START, GAME_H_END))
        pygame.draw.line(display, Colors.WHITE.value, (GAME_W_END, GAME_H_START), (GAME_W_END, GAME_H_END))
        pygame.draw.line(display, Colors.WHITE.value, (GAME_W_START, GAME_H_START), (GAME_W_END, GAME_H_START))
        pygame.draw.line(display, Colors.WHITE.value, (GAME_W_START, GAME_H_END), (GAME_W_END, GAME_H_END))

    def draw_score(self, display: Surface) -> None:
        font: Font = SysFont('Source Code Variable', 30)
        score_text: Surface = font.render(f'Score: {self.game.score}', True, Colors.WHITE.value)
        display.blit(score_text, (70, WINDOW_W // 6))

    def draw_next_tetromino(self, display: Surface) -> None:
        pygame.draw.line(display, Colors.WHITE.value, (-10 + NEXT_TETROMINO_W_START, -10 + NEXT_TETROMINO_H_START), (-10 + NEXT_TETROMINO_W_START, 10 + NEXT_TETROMINO_H_END))
        pygame.draw.line(display, Colors.WHITE.value, (10 + NEXT_TETROMINO_W_END, -10 + NEXT_TETROMINO_H_START), (10 + NEXT_TETROMINO_W_END, 10 + NEXT_TETROMINO_H_END))
        pygame.draw.line(display, Colors.WHITE.value, (-10 + NEXT_TETROMINO_W_START, -10 + NEXT_TETROMINO_H_START), (10 + NEXT_TETROMINO_W_END, -10 + NEXT_TETROMINO_H_START))
        pygame.draw.line(display, Colors.WHITE.value, (-10 + NEXT_TETROMINO_W_START, 10 + NEXT_TETROMINO_H_END), (10 + NEXT_TETROMINO_W_END, 10 + NEXT_TETROMINO_H_END))
        #for tetromino in self.game.next_tetrominos
        self.draw_tetromino(display, NEXT_TETROMINO_W_START, NEXT_TETROMINO_H_START, self.game.next_tetrominos[0])

    def draw_current_tetromino(self, display: Surface) -> None:
        x = GAME_W_START + (self.game.current_tetromino.x * BRICK_SIZE)
        y = GAME_H_START + (self.game.current_tetromino.y * BRICK_SIZE)
        self.draw_tetromino(display, x, y, self.game.current_tetromino)

    def draw_tetromino(self, display: Surface, x_offset: int, y_offset: int, tetromino: Tetromino):
        for i in range(4):
            for j in range(4):
                if tetromino.get_shape()[i][j] == ' ':
                    continue
                x = x_offset + (j * BRICK_SIZE)
                y = y_offset + (i * BRICK_SIZE)
                pygame.draw.rect(display, Colors.RED.value, (x, y, BRICK_SIZE, BRICK_SIZE))
