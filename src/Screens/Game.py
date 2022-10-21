import pygame
from pygame.surface import Surface
from pygame.font import SysFont, Font

from copy import copy

from Options.Options import  BRICK_SIZE, GAME_H_START, GAME_W_START, GAME_H_END, GAME_W_END, WINDOW_W, NEXT_TETROMINO_H, NEXT_TETROMINO_W, TETROMINO_SHOWN, HOLD_TETROMINO_H, HOLD_TETROMINO_W, BORDER, OFFSCREEN_BRICK_SIZE, TETROMINO_SHADOW
from Options.Colors import Colors, Color_mod
from Tetromino.Tetromino import Tetromino
from Tetromino.Brick import Brick, Standard_brick, Line_brick, Shiny_brick, Open_brick, Border_brick
from Screens.Screen import State
from Screens.Content import Content
from Logic.Logic import Logic
from Tetromino.Shape import Shape

class Game(Content):
    def __init__(self) -> None:
        self.game: Logic = Logic()
        self.border: int = BORDER
        self.brick_size: int = OFFSCREEN_BRICK_SIZE
        self.brick_skin: Brick = Shiny_brick() # Standard_brick(), Line_brick(), Shiny_brick(), Border_brick()

    def update(self, display: Surface) -> State:
        exit: State = self.game.input_action()
        if exit == State.Title: return exit
        # TODO Game over
        if not self.game.check_alive():
            return State.Title
        return State.Stay

    def draw(self, display: Surface) -> None:
        self.draw_stats(display)
        self.draw_score(display)
        self.draw_next_tetromino(display)
        self.draw_swap_tetromino(display)
        self.draw_grid(display)
        if TETROMINO_SHADOW: self.draw_shadow_tetromino(display)
        self.draw_current_tetromino(display)
        self.draw_border(display)

    def draw_grid(self, display: Surface) -> None:
        for i in range(2, len(self.game.grid)):
            for j in range(len(self.game.grid[i])):
                if self.game.grid[i][j] != Colors.BLACK.value:
                    self.brick_skin.draw_brick(display,
                                               GAME_W_START + (j * BRICK_SIZE),
                                               GAME_H_START + (i * BRICK_SIZE),
                                               BRICK_SIZE,
                                               self.game.grid[i][j])
                else:
                    pygame.draw.rect(display,
                                     self.game.grid[i][j],
                                     (GAME_W_START + (j * BRICK_SIZE),
                                     GAME_H_START + (i * BRICK_SIZE),
                                     BRICK_SIZE,
                                     BRICK_SIZE))

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
        pygame.draw.rect(display,
                         Colors.WHITE.value,
                         (GAME_W_START, GAME_H_START + (2 * BRICK_SIZE),
                         (10 * BRICK_SIZE), (20 * BRICK_SIZE)),
                         width=2
                         )

    def draw_stats(self, display: Surface) -> None:
        font: Font = SysFont('Source Code Variable', 25)
        i: int = 1
        for shape in Shape:
            tetromino: Surface = font.render(f'{shape.name}: {self.game.generator.counter[shape]}', True, Colors.WHITE.value)
            display.blit(tetromino, (WINDOW_W // 12, 300 + (i * 50)))
            i += 1


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
                                self.game.next_tetrominos[i].get_shape(),
                                self.game.next_tetrominos[i].color.value,
                                self.brick_size)

    def draw_swap_tetromino(self, display: Surface) -> None:
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
                                self.game.hold_tetromino.get_shape(),
                                self.game.hold_tetromino.color.value,
                                self.brick_size)

    def draw_current_tetromino(self, display: Surface) -> None:
        if not self.game.current_tetromino: return

        x = GAME_W_START + (self.game.current_tetromino.x * BRICK_SIZE)
        y = GAME_H_START + (self.game.current_tetromino.y * BRICK_SIZE)
        self.draw_tetromino(display,
                            x,
                            y,
                            self.game.current_tetromino.get_shape(),
                            self.game.current_tetromino.color.value)

    def draw_shadow_tetromino(self, display: Surface):
        if not self.game.current_tetromino: return

        shadow_tetromino: Tetromino = copy(self.game.current_tetromino)
        shadow_tetromino.hard_drop(self.game.grid)
        x = GAME_W_START + (shadow_tetromino.x * BRICK_SIZE)
        y = GAME_H_START + (shadow_tetromino.y * BRICK_SIZE)
        self.draw_tetromino(display,
                            x,
                            y,
                            shadow_tetromino.get_shape(),
                            Color_mod().get_shadow_from_color(shadow_tetromino.color),
                            BRICK_SIZE,
                            shadow=True)

    def draw_tetromino(self,
                       display: Surface,
                       x_offset: int,
                       y_offset: int,
                       shape: list[str],
                       color: tuple[int,int,int],
                       brick_size: int = BRICK_SIZE,
                       shadow: bool = False):
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] == ' ':
                    continue

                x = x_offset + (j * brick_size)
                y = y_offset + (i * brick_size)

                if y < GAME_H_START + (2 * brick_size):
                    continue

                self.brick_skin.draw_brick(display,
                                      x,
                                      y,
                                      brick_size,
                                      color,
                                      shadow)

