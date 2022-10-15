import pygame
from pygame.locals import K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_SPACE
from pygame.locals import KEYUP, KEYDOWN

from random import randint, shuffle
from itertools import cycle

from Tetromino import Shape, Tetromino
from Options import FALL_SPEED, TETROMINO_SHOWN, KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL

class Logic():
    def __init__(self) -> None:
        self.frames: int = 0
        self.score: int = 0
        self.tetrominos: dict[int, Tetromino] = dict(zip(range(len(Shape)), [Tetromino(shape) for shape in Shape]))
        self.grid: list[list] = [[(0,0,0) for _ in range(10)] for _ in range(20)]
        self.hold_tetromino: Tetromino
        self.current_tetromino: Tetromino
        self.next_tetrominos: list[Tetromino] = []
        self.next_tetromino()

    def next_tetromino(self) -> None:
        if len(self.next_tetrominos) == 0:
            self.generate_next_tetrominos()
        self.current_tetromino = self.next_tetrominos.pop()

    def generate_next_tetrominos(self) -> None:
        sequence = [*range(len(Shape))]
        shuffle(sequence)
        sequence = sequence[:TETROMINO_SHOWN]
        for i in sequence:
            self.next_tetrominos.append(self.tetrominos[i % len(sequence)])

    def input_action(self) -> None:
        self.frames += 1
        if self.frames % FALL_SPEED == 0:
            self.frames = 0
            self.current_tetromino.down(self.grid)

        key = pygame.key.get_pressed()
        if key[K_h]:
            self.current_tetromino.left(self.grid)
        if key[K_j]:
            self.current_tetromino.down(self.grid)
        if key[K_k]:
            self.current_tetromino.rotate_180(self.grid)
        if key[K_l]:
            self.current_tetromino.right(self.grid)
        if key[K_SPACE]:
            self.current_tetromino.hard_drop(self.grid)
        if key[K_z]:
            self.current_tetromino.rotate_left(self.grid)
        if key[K_x]:
            self.current_tetromino.rotate_right(self.grid)
        if key[K_c]:
            self.change_tetromino()

        # Remover e colocar em opcoes no Title()
        #pygame.key.set_repeat(KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL)

        # For some reason it just dont work
        #e = pygame.event.wait()
        #    print(e)
        #    if e.type == pygame.TEXTINPUT:
        #        if e.text == 'h':
        #            self.current_tetromino.left(self.grid)
        #        if e.text == 'j':
        #            self.current_tetromino.down(self.grid)
        #        if e.text == 'k':
        #            self.current_tetromino.rotate_180(self.grid)
        #        if e.text == 'l':
        #            self.current_tetromino.right(self.grid)
        #if e.type == KEYDOWN:
        #    if e.key == pygame.K_h:
        #        self.current_tetromino.left(self.grid)
        #    if e.key == K_j:
        #        self.current_tetromino.down(self.grid)
        #    if e.key == K_k:
        #        self.current_tetromino.rotate_180(self.grid)
        #    if e.key == K_l:
        #        self.current_tetromino.right(self.grid)
        #    if e.key == K_SPACE:
        #        self.current_tetromino.hard_drop(self.grid)
        #    if e.key == K_z:
        #        self.current_tetromino.rotate_left(self.grid)
        #    if e.key == K_x:
        #        self.current_tetromino.rotate_right(self.grid)
        #    if e.key == K_c:
        #        self.change_tetromino()

    def change_tetromino(self):
        self.current_tetromino.reset()
        self.hold_tetromino = self.current_tetromino
        self.next_tetromino()

    #def random_tetromino(self) -> Tetromino:
    #    return self.tetrominos[randint(0, len(Shape))]
