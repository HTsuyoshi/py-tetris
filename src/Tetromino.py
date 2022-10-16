from Shape import Shape
from Colors import Colors, Color_mod

class SRS:
    # SRS System (J,L,S,T,Z)
    #   Offset 1 Offset 2 Offset 3 Offset 4 Offset 5
    # 0 ( 0, 0)  ( 0, 0)  ( 0, 0)  ( 0, 0)  ( 0, 0)
    # R ( 0, 0)  (+1, 0)  (+1,-1)  ( 0,+2)  (+1,+2)
    # 2 ( 0, 0)  ( 0, 0)  ( 0, 0)  ( 0, 0)  ( 0, 0)
    # L ( 0, 0)  (-1, 0)  (-1,-1)  ( 0,+2)  (-1,+2)
    # SRS System (I)
    #   Offset 1 Offset 2 Offset 3 Offset 4 Offset 5
    # 0 ( 0, 0)  (-1, 0)  (+2, 0)  (-1, 0)  (+2, 0)
    # R (-1, 0)  ( 0, 0)  ( 0, 0)  ( 0,+1)  ( 0,-2)
    # 2 (-1,+1)  (+1,+1)  (-2,+1)  (+1, 0)  (-2, 0)
    # L ( 0,+1)  ( 0,+1)  ( 0,+1)  ( 0,-1)  ( 0,+2)
    # SRS System (O)
    #   Offset 1
    # 0 ( 0, 0)
    # R ( 0, -1)
    # 2 ( -1, -1)
    # L ( -1, 0)
    def __init__(self, shape: Shape):
        if shape == Shape.SHAPE_I:
            self.rot = [
                    [(0, 0), (-1, 0), (2, 0), (-1, 0), (2, 0)],
                    [(-1, 0), ( 0, 0), ( 0, 0), ( 0, 1), ( 0, -2)],
                    [(-1, 1), (1, 1), (-2, 1), (1, 0), (-2, 0)],
                    [(0, 1), (0, 1), (0, 1), (0, -1), ( 0, 2)]
                    ]
        elif shape == Shape.SHAPE_O:
            self.rot = [
                    [(0, 0)],
                    [(0, -1)],
                    [(-1, -1)],
                    [(-1, 0)]
                    ]
        else:
            self.rot = [
                    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
                    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)]
                    ]

class Tetromino:
    def __init__(self, shape: Shape) -> None:
        self.x: int = 3
        self.y: int = 0
        self.shape: Shape = shape
        self.rotation: int = 0
        self.color: Colors = Color_mod().get_color[shape]

    def get_shape(self) -> list[str]:
        return self.shape.value[self.rotation % len(self.shape.value)]

    def right(self, grid: list[list[tuple[int,int,int]]]) -> bool:
        if self.check(self.x + 1,
                      self.y,
                      self.rotation,
                      grid):
            self.x += 1
            return True
        return False

    def left(self, grid: list[list[tuple[int,int,int]]]) -> bool:
        if self.check(self.x - 1,
                      self.y,
                      self.rotation,
                      grid):
            self.x -= 1
            return True
        return False

    def down(self, grid: list[list[tuple[int,int,int]]]) -> bool:
        if self.check(self.x,
                      self.y + 1,
                      self.rotation,
                      grid):
            self.y += 1
            return True
        return False

    def hard_drop(self, grid: list[list[tuple[int,int,int]]]) -> None:
        if self.down(grid):
            self.hard_drop(grid)

    def rotate_180(self, grid: list[list[tuple[int,int,int]]]) -> bool:
        if self.check(self.x,
                      self.y,
                      self.rotation + 2,
                      grid):
            self.rotation += 2
            return True
        return False

    def rotate_right(self, grid: list[list[tuple[int,int,int]]]) -> bool:
        next: int = (self.rotation + 1) % 4
        if self.check(self.x,
                      self.y,
                      next,
                      grid):
            self.rotation = next
            return True

        kick_system: SRS = SRS(self.shape)
        test_list: list[tuple[int,int]] = []

        for c, n in zip(kick_system.rot[self.rotation], kick_system.rot[next]):
            test_list.append((c[0] - n[0], c[1] - n[1]))

        for test in test_list:
            if self.check(self.x + test[0],
                          self.y + test[1],
                          next,
                          grid):
                self.x += test[0]
                self.y += test[1]
                self.rotation = next
                return True
        return False

    def rotate_left(self, grid: list[list[tuple[int,int,int]]]) -> bool:
        next: int = (self.rotation - 1) % 4
        if self.check(self.x,
                      self.y,
                      next,
                      grid):
            self.rotation = next
            return True

        kick_system: SRS = SRS(self.shape)
        test_list: list[tuple[int,int]] = []

        for c, n in zip(kick_system.rot[self.rotation], kick_system.rot[next]):
            test_list.append((c[0] + n[0], c[1] + n[1]))

        for test in test_list:
            if self.check(self.x + test[0],
                          self.y + test[1],
                          next,
                          grid):
                self.x += test[0]
                self.y += test[1]
                self.rotation = next
                return True

        return False

    def check(self,
              x: int,
              y: int,
              rotation: int,
              grid: list[list[tuple[int,int,int]]]) -> bool:

        new_tetromino: list[str] = self.shape.value[rotation % len(self.shape.value)]
        for i in range(4):
            for j in range(4):
                if x + j >= len(grid[0]) or y + i >= len(grid):
                    continue
                if new_tetromino[i][j] == 'o' and grid[y + i][x + j] != Colors.BLACK.value:
                    return False

        max_left: int = min(i.find('o') for i in new_tetromino if i.find('o') != -1)
        if x + max_left < 0:
            return False

        max_right: int = max(i.rfind('o') for i in new_tetromino if i.find('o') != -1)
        if x + max_right >= len(grid[0]):
            return False

        max_down: int = max(i for i in range(4) if new_tetromino[i].find('o') != -1)
        if y + max_down >= len(grid):
            return False

        return True

    def reset(self):
        self.x = 3
        self.y = 0
        self.rotation = 0
