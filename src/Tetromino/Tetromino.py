from Tetromino.Shape import Shape
from Options.Colors import Colors, Color_mod

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

class SRS:
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
        self.lowest_y: int = 0
        self.reset_delay_bool: bool = False
        self.shape: Shape = shape
        self.rotation: int = 0
        self.color: Colors = Color_mod().get_color[shape]

    def get_shape(self) -> list[str]:
        return self.shape.value[self.rotation % len(self.shape.value)]

    def move(self,
             grid: list[list[tuple[int,int,int]]],
             x: int,
             y: int) -> bool:
        if self.check(self.x + x,
                      self.y + y,
                      self.rotation,
                      grid):
            self.x += x
            self.y += y
            if self.y > self.lowest_y:
                self.lowest_y = self.y
                self.reset_delay_bool = True
            return True
        return False

    def down(self, grid) -> bool:
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

    def rotate(self,
               grid: list[list[tuple[int,int,int]]],
               rotation: int) -> bool:
        next: int = (self.rotation + rotation) % 4
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
                          self.y - test[1],
                          next,
                          grid):
                self.x += test[0]
                self.y -= test[1]
                self.rotation = next
                return True
        return False

    def check(self,
              x: int,
              y: int,
              rotation: int,
              grid: list[list[tuple[int,int,int]]]) -> bool:

        new_tetromino: list[str] = self.shape.value[rotation % len(self.shape.value)]

        for i in range(len(new_tetromino)):
            for j in range(len(new_tetromino)):
                if new_tetromino[i][j] == ' ':
                    continue
                if x + j < 0 or x + j >= len(grid[0]) or y + i >= len(grid):
                    return False
                if grid[y + i][x + j] != Colors.BLACK.value:
                    return False
        return True

    def reset(self) -> None:
        self.x = 3
        self.y = 0
        self.lowest_y = 0
        self.rotation = 0

    def reset_delay(self) -> bool:
        if self.reset_delay_bool:
            self.reset_delay_bool = False
            return True
        return False
