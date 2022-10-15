import abc
from pygame.surface import Surface

class Content(abc.ABC):
    @abc.abstractclassmethod
    def update(self, display: Surface) -> None:
        pass

    @abc.abstractclassmethod
    def draw(self, display: Surface) -> None:
        pass
