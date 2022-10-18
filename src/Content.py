from pygame.surface import Surface

import abc
from enum import Enum

class State(Enum):
    Stay = -1
    Title = 0
    Game = 1

class Content(abc.ABC):
    @abc.abstractclassmethod
    def update(self, display: Surface) -> State:
        return State.Stay

    @abc.abstractclassmethod
    def draw(self, display: Surface) -> None:
        pass
