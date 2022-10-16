import abc
from random import randint

from Tetromino import Tetromino
from Shape import Shape
from copy import copy

class Randomizer(abc.ABC):
    def __init__(self):
        self.tetrominos: dict[int, Tetromino] = dict(zip(range(len(Shape)), [Tetromino(shape) for shape in Shape]))
        self.tries: int = 6

    @abc.abstractclassmethod
    def get_random(self) -> Tetromino:
        return copy(self.tetrominos[randint(0,len(self.tetrominos.keys()) - 1)])

class TGM(Randomizer):
    def __init__(self):
        self.tetrominos: dict[int, Tetromino] = dict(zip(range(len(Shape)), [Tetromino(shape) for shape in Shape]))
        self.tries: int = 6
        self.first: bool = True

    def get_random(self, history: list[Tetromino]) -> Tetromino:
        default: list[Tetromino] = [Tetromino(Shape.SHAPE_Z), Tetromino(Shape.SHAPE_Z), Tetromino(Shape.SHAPE_S), Tetromino(Shape.SHAPE_S)]
        while len(history) < 4:
            history.append(default.pop(0))

        tetromino: Tetromino = Tetromino(Shape.SHAPE_I)
        for _ in range(self.tries):
            tetromino = copy(self.tetrominos[randint(0,len(self.tetrominos.keys()) - 1)])
            if tetromino not in history:
                if self.first:
                    if tetromino.shape.value in [Shape.SHAPE_Z.value, Shape.SHAPE_S.value, Shape.SHAPE_O.value]:
                        continue
                break

        self.first = False
        return tetromino
