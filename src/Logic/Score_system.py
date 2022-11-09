import abc

from Tetromino.Tetromino import Tetromino
from Tetromino.Shape import Shape

class Score_system(abc.ABC):
    def __init__(self):
        self.score: int = 0
        self.attack: int = 0

    @abc.abstractclassmethod
    def add_score(self, lines:int, t_spin: bool) -> None:
        pass

    @abc.abstractclassmethod
    def add_attack(self, lines:int, t_spin: bool, combo: int) -> None:
        pass

class Classic_score(Score_system):
    def __init__(self):
        self.score: int = 0
        self.attack: int = 0

    def add_score(self, lines: int, t_spin: bool) -> None:
        self.score += lines * 100

    def add_attack(self, lines:int, t_spin: bool, combo: int) -> None:
        pass

class Modern_score(Score_system):
    def __init__(self):
        self.score: int = 0
        self.attack: int = 0

    def add_score(self, lines: int, t_spin: bool) -> None:
        self.score += lines * 100

    def add_attack(self, lines: int, t_spin: bool, combo: int) -> None:
        attack: int = 0

        if combo > 1:
            if combo in [2, 3, 4]:
                print(attack)
                attack = max(1, attack)
            elif combo in [5, 6]:
                attack = max(2, attack)
            elif combo in [7, 8]:
                attack = max(3, attack)
            elif combo in [9, 10, 11]:
                attack = max(4, attack)
            else:
                attack = max(5, attack)

        if t_spin:
            if lines == 1:
                attack = max(2, attack)
            elif lines == 2:
                attack = max(4, attack)
            elif lines == 3:
                attack = max(6, attack)

        else:
            if lines == 2:
                attack = max(1, attack)
            elif lines == 3:
                attack = max(2, attack)
            elif lines == 4:
                attack = max(4, attack)

        self.attack += attack
