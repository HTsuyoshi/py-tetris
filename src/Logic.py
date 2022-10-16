import pygame
from pygame.locals import K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_a, K_SPACE
from pygame.locals import KEYUP, KEYDOWN

from typing import Optional
from copy import copy

from Options import FALL_SPEED, LOCK_DELAY, TETROMINO_SHOWN, KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL, SOFT_DROP, Soft_drop
from Shape import Shape
from Tetromino import Tetromino
from Randomizer import Randomizer, TGM
from Colors import Colors, Color_mod

class Tetromino_generator:
    def __init__(self):
        self.counter: dict[Shape, int] = {
                Shape.SHAPE_J: 0,
                Shape.SHAPE_L: 0,
                Shape.SHAPE_S: 0,
                Shape.SHAPE_Z: 0,
                Shape.SHAPE_I: 0,
                Shape.SHAPE_O: 0,
                Shape.SHAPE_T: 0
                }
        self.randomizer: Randomizer = TGM()
        self.history: list[Tetromino] = []

    def next_tetromino(self) -> Tetromino:
        tetromino: Tetromino = self.randomizer.get_random(self.history)
        self.counter[tetromino.shape] += 1
        return tetromino

    def add_history(self, tetromino: Tetromino):
        self.history.append(tetromino)
        if len(self.history) > 4:
            self.history.pop(0)

class Logic():
    def __init__(self):
        self.frames: int = 0
        self.score: int = 0
        self.grid: list[list[tuple[int,int,int]]] = [[(0,0,0) for _ in range(10)] for _ in range(22)]
        self.current_tetromino: Optional[Tetromino] = None
        self.can_change: bool = True
        self.hold_tetromino: Optional[Tetromino] = None
        self.next_tetrominos: list[Tetromino] = []
        self.generator: Tetromino_generator = Tetromino_generator()
        self.next_tetromino()

    def input_action(self) -> None:
        if not self.current_tetromino: return

        self.frames += 1
        if self.frames % FALL_SPEED == 0:
            self.current_tetromino.down(self.grid)

        if self.frames % LOCK_DELAY == 0:
            self.frames = 0
            self.lock_tetromino()

        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_h:
                    self.current_tetromino.left(self.grid)
                elif e.key == K_j:
                    if SOFT_DROP == Soft_drop.NORMAL: self.current_tetromino.down(self.grid)
                    elif SOFT_DROP == Soft_drop.INSTANT: self.current_tetromino.hard_drop(self.grid)
                elif e.key == K_k:
                    self.current_tetromino.rotate_180(self.grid)
                elif e.key == K_l:
                    self.current_tetromino.right(self.grid)
                elif e.key == K_SPACE:
                    self.current_tetromino.hard_drop(self.grid)
                    self.lock_tetromino()
                elif e.key == K_z:
                    self.current_tetromino.rotate_left(self.grid)
                elif e.key == K_x:
                    self.current_tetromino.rotate_right(self.grid)
                elif e.key == K_c:
                    self.change_tetromino()
                elif e.key == K_a:
                    self.lock_tetromino()

    def next_tetromino(self) -> None:
        while len(self.next_tetrominos) < TETROMINO_SHOWN + 1:
            self.next_tetrominos.append(self.generator.next_tetromino())
        self.current_tetromino = self.next_tetrominos.pop(0)

    def change_tetromino(self) -> None:
        if not self.can_change: return
        if not self.current_tetromino: return
        self.current_tetromino.reset()

        tetromino: Optional[Tetromino] = None
        if self.hold_tetromino: tetromino = self.hold_tetromino

        self.hold_tetromino = self.current_tetromino
        self.can_change = False
        self.frames = 0

        if tetromino:
            self.current_tetromino = tetromino
            return

        self.next_tetromino()

    def lock_tetromino(self) -> None:
        if not self.current_tetromino:
            return

        for i in range(4):
            for j in range(4):
                if self.current_tetromino.x + j > len(self.grid[0]) or self.current_tetromino.y + i > len(self.grid):
                    continue
                if self.current_tetromino.get_shape()[i][j] == 'o':
                    self.grid[self.current_tetromino.y + i][self.current_tetromino.x + j] = Color_mod().get_color[self.current_tetromino.shape].value

        self.can_change = True
        self.generator.add_history(self.current_tetromino)
        self.frames = 0
        self.clear_row()
        self.next_tetromino()

    def clear_row(self) -> None:
        for row in range(len(self.grid)):
            if Colors.BLACK.value not in self.grid[row]:
                self.grid.remove(self.grid[row])
                self.grid.insert(0, [Colors.BLACK.value for _ in range(10)])

    def check_alive(self) -> bool:
        if not self.current_tetromino: return False
        return self.current_tetromino.check(self.current_tetromino.x,
                                            self.current_tetromino.y,
                                            self.current_tetromino.rotation,
                                            self.grid)
