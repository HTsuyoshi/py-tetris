import abc
from random import randint

from Tetromino import Tetromino
from Shape import Shape
from copy import copy

class Randomizer(abc.ABC):
    @abc.abstractclassmethod
    def get_random(self) -> Tetromino:
        tetrominos: dict[int, Tetromino] = dict(zip(range(len(Shape)), [Tetromino(shape) for shape in Shape]))
        return copy(tetrominos[randint(0,len(tetrominos.keys()) - 1)])

class Classic_tetris(Randomizer):
    def __init__(self):
        self.tetrominos: dict[int, Tetromino] = dict(zip(range(len(Shape)), [Tetromino(shape) for shape in Shape]))

    def get_random(self, history: list[Shape]) -> Tetromino:
        return copy(self.tetrominos[randint(0,len(self.tetrominos.keys()) - 1)])

class TGM(Randomizer):
    def __init__(self):
        self.tetrominos: dict[int, Shape] = dict(zip(range(len(Shape)), [shape for shape in Shape]))
        self.tries: int = 6
        self.first: bool = True

    def get_random(self, history: list[Shape]) -> Tetromino:
        default: list[Shape] = [Shape.SHAPE_Z, Shape.SHAPE_Z, Shape.SHAPE_S, Shape.SHAPE_S]
        local_history: list[Shape] = []
        local_history.extend(history)

        while len(local_history) < 4:
            local_history.append(default.pop(0))

        shape: Shape = self.tetrominos[0]
        for _ in range(self.tries):
            shape = self.tetrominos[randint(0,len(self.tetrominos.keys()) - 1)]
            if shape not in local_history:
                if self.first:
                    if shape in [Shape.SHAPE_Z, Shape.SHAPE_S, Shape.SHAPE_O]:
                        continue
                self.first = False
                break

        return Tetromino(shape)
