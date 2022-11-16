import pygame
from pygame.locals import K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_a, K_q, K_SPACE
from pygame.locals import KEYDOWN

from typing import Optional
from enum import Enum

from Options.Options import FALL_SPEED, LOCK_DELAY, TETROMINO_SHOWN, KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL, SOFT_DROP, Soft_drop, GARBAGE_SPEED
from Options.Colors import Colors, Color_mod
from Tetromino.Shape import Shape
from Tetromino.Tetromino import Tetromino
from Logic.Randomizer import Randomizer, TGM, Classic_tetris, Modern_tetris
from Logic.Score_system import Score_system, Classic_score, Modern_score
from Screens.Screen import State

class Game_mode(Enum):
    Classic = 0
    Garbage_mode = 1
    Training = 2

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
        self.randomizer: Randomizer = Modern_tetris() #TGM(), Classic_tetris, Modern_tetris
        self.history: list[Shape] = []

    def next_tetromino(self) -> Tetromino:
        tetromino: Tetromino = self.randomizer.get_random(self.history)
        self.add_history(tetromino)
        self.counter[tetromino.shape] += 1
        return tetromino

    def add_history(self, tetromino: Tetromino):
        self.history.append(tetromino.shape)
        if len(self.history) > 4:
            self.history.pop(0)

class Logic():
    def __init__(self, game_mode: Game_mode):
        self.game_mode: Game_mode = game_mode
        self.lock_delay: int = LOCK_DELAY
        self.frames: int = 0
        self.score: Score_system = Modern_score() # Classic_score()
        self.generator: Tetromino_generator = Tetromino_generator()
        self.combo: int = 0
        self.grid: list[list[tuple[int,int,int]]] = [[(0,0,0) for _ in range(10)] for _ in range(22)]
        self.can_swap: bool = True
        self.current_tetromino: Optional[Tetromino] = None
        self.hold_tetromino: Optional[Tetromino] = None
        self.next_tetrominos: list[Tetromino] = []
        self.next_tetromino()

    def input_action(self) -> State:
        if not self.current_tetromino: return State.Stay

        self.lock_delay -= 1
        self.frames += 1
        if self.frames % FALL_SPEED == 0:
            self.current_tetromino.move(self.grid, 0, 1)

        if self.game_mode == Game_mode.Garbage_mode:
            if self.frames % GARBAGE_SPEED == 0:
                self.add_garbage()

        if self.current_tetromino.reset_delay():
            self.lock_delay = LOCK_DELAY

        if self.lock_delay < 0:
            self.lock_delay = LOCK_DELAY
            self.current_tetromino.hard_drop(self.grid)
            self.lock_tetromino()

        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_h:
                    self.current_tetromino.move(self.grid, -1, 0)
                elif e.key == K_l:
                    self.current_tetromino.move(self.grid, 1, 0)
                elif e.key == K_k:
                    self.current_tetromino.rotate_180(self.grid)
                elif e.key == K_j:
                    if SOFT_DROP == Soft_drop.NORMAL: self.current_tetromino.move(self.grid, 0, 1)
                    elif SOFT_DROP == Soft_drop.INSTANT: self.current_tetromino.hard_drop(self.grid)
                elif e.key == K_SPACE:
                    self.current_tetromino.hard_drop(self.grid)
                    self.lock_tetromino()
                elif e.key == K_z:
                    self.current_tetromino.rotate(self.grid, -1)
                elif e.key == K_x:
                    self.current_tetromino.rotate(self.grid, 1)
                elif e.key == K_c:
                    self.swap_tetromino()
                elif e.key == K_a:
                    self.lock_tetromino()
                elif e.key == K_q:
                    return State.Title
        return State.Stay

    def next_tetromino(self) -> None:
        while len(self.next_tetrominos) < TETROMINO_SHOWN + 1:
            self.next_tetrominos.append(self.generator.next_tetromino())
        self.current_tetromino = self.next_tetrominos.pop(0)

    def swap_tetromino(self) -> None:
        if not self.can_swap: return
        if not self.current_tetromino: return
        self.current_tetromino.reset()

        tetromino: Optional[Tetromino] = None
        if self.hold_tetromino: tetromino = self.hold_tetromino

        self.hold_tetromino = self.current_tetromino
        self.can_swap = False

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

        self.can_swap = True
        if not self.clear_row(): self.combo = 0
        self.next_tetromino()

    def is_t_spin(self) -> bool:
        if not self.current_tetromino:
            return False

        if not self.current_tetromino.shape.value == Shape.SHAPE_T.value:
            return False

        occupied_blocks: int = 0

        def verify_occupied(x: int, y: int) -> int:
            if y >= len(self.grid) or x >= len(self.grid[0]): return 1
            if self.grid[y][x] != Colors.BLACK: return 1
            return 0

        x: int = self.current_tetromino.x
        y: int = self.current_tetromino.y
        occupied_blocks += verify_occupied(x, y)
        occupied_blocks += verify_occupied(x + 2, y)
        occupied_blocks += verify_occupied(x, y + 2)
        occupied_blocks += verify_occupied(x + 2, y + 2)

        if occupied_blocks > 2: return True
        return False

    def clear_row(self) -> bool:
        if not self.current_tetromino:
            return False

        t_spin: bool = self.is_t_spin()

        # Normal Score
        lines: int = 0
        for row in range(len(self.grid)):
            if Colors.BLACK.value not in self.grid[row]:
                lines += 1
                self.grid.remove(self.grid[row])
                self.grid.insert(0, [Colors.BLACK.value for _ in range(10)])

        if lines > 0:
            self.score.add_score(lines, t_spin)
            self.score.add_attack(lines, t_spin, self.combo)
            self.combo += 1
            return True
        return False

    def add_garbage(self) -> None:
        if self.current_tetromino:
            from copy import copy
            new_grid = copy(self.grid)
            new_grid.pop(0)
            garbage: list[tuple[int,int,int]] = [(127, 127, 127)] * len(self.grid[0])
            from random import randint
            garbage[randint(0, len(self.grid[0]) - 1)] = (0, 0, 0)
            new_grid.append(garbage)
            if not self.current_tetromino.check(self.current_tetromino.x,
                                                self.current_tetromino.y,
                                                self.current_tetromino.rotation,
                                                new_grid):
                self.current_tetromino.move(self.grid, 0, -1)
            self.grid = new_grid

    def check_alive(self) -> bool:
        if not self.current_tetromino: return False
        return self.current_tetromino.check(self.current_tetromino.x,
                                            self.current_tetromino.y,
                                            self.current_tetromino.rotation,
                                            self.grid)
