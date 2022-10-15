from Shape import Shape

class Tetromino:
    def __init__(self, shape: Shape) -> None:
        self.x: int = 3
        self.y: int = 0
        self.shape: Shape = shape
        self.rotation: int = 0

    def get_shape(self) -> list[str]:
        return self.shape.value[self.rotation % len(self.shape.value)]

    def right(self, grid: list[list[str]]) -> bool:
        if self.check(self.x + 1, self.y, self.rotation, grid):
            self.x += 1
            return True
        return False

    def left(self, grid: list[list[str]]) -> bool:
        if self.check(self.x - 1, self.y, self.rotation, grid):
            self.x -= 1
            return True
        return False

    def down(self, grid: list[list[str]]) -> bool:
        if self.check(self.x, self.y + 1, self.rotation, grid):
            self.y += 1
            return True
        return False

    def hard_drop(self, grid: list[list[str]]) -> None:
        if self.down(grid):
            self.hard_drop(grid)

    def rotate_180(self, grid: list[list[str]]) -> bool:
        if self.check(self.x, self.y, self.rotation + 2, grid):
            self.rotation += 2
            return True
        return False

    # Wallkick tests for J, L, S, T, Z
    #          1       2       3       4       5
    # 0->R	( 0, 0)	(-1, 0)	(-1,+1)	( 0,-2)	(-1,-2)
    # R->2	( 0, 0)	(+1, 0)	(+1,-1)	( 0,+2)	(+1,+2)
    # 2->L	( 0, 0)	(+1, 0)	(+1,+1)	( 0,-2)	(+1,-2)
    # L->0	( 0, 0)	(-1, 0)	(-1,-1)	( 0,+2)	(-1,+2)
    # 0 = 0; R = 1; 2 = 2; L = 3

    # Wallkick tests for I
    #          1       2       3       4       5
    #0->R	( 0, 0)	(-2, 0)	(+1, 0)	(-2,-1)	(+1,+2)
    #R->2	( 0, 0)	(-1, 0)	(+2, 0)	(-1,+2)	(+2,-1)
    #2->L	( 0, 0)	(+2, 0)	(-1, 0)	(+2,+1)	(-1,-2)
    #L->0	( 0, 0)	(+1, 0)	(-2, 0)	(+1,-2)	(-2,+1)

    def rotate_right(self, grid: list[list[str]]) -> bool:
        if self.check(self.x, self.y, self.rotation + 1, grid):
            self.rotation += 1
            return True

        tests: list[tuple[int,int]] = [(-1,-1)]
        if self.shape == Shape.SHAPE_L:
            if self.rotation == 0:
                tests = [( 0, 0), (-2, 0), (+1, 0), (-2,-1), (+1,+2)]
            if self.rotation == 1:
                tests = [( 0, 0), (-1, 0), (+2, 0), (-1,+2), (+2,-1)]
            if self.rotation == 2:
                tests = [( 0, 0), (+2, 0), (-1, 0), (+2,+1), (-1,-2)]
            if self.rotation == 3:
                tests = [( 0, 0), (+1, 0), (-2, 0), (+1,-2), (-2,+1)]
        else:
            if self.rotation == 0:
                tests = [(0, 0), (-2, 0), (1, 0), (2, -1), (1, 2)]
            if self.rotation == 1:
                tests = [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)]
            if self.rotation == 2:
                tests = [(0, 0), (2, 0), (-1, 0), (2, 1), (-1,-2)]
            if self.rotation == 3:
                tests = [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)]

        for test in tests:
            if self.check(self.x + test[0], self.y + test[1], self.rotation - 1, grid):
                self.x += test[0]
                self.y += test[1]
                self.rotation += 1
                return True

        return False

    # Wallkick tests for J, L, S, T, Z
    #          1       2       3       4       5
    # L->2	( 0, 0)	(-1, 0)	(-1,-1)	( 0,+2)	(-1,+2)
    # 2->R	( 0, 0)	(-1, 0)	(-1,+1)	( 0,-2)	(-1,-2)
    # R->0	( 0, 0)	(+1, 0)	(+1,-1)	( 0,+2)	(+1,+2)
    # 0->L	( 0, 0)	(+1, 0)	(+1,+1)	( 0,-2)	(+1,-2)

    # Wallkick tests for I
    #          1       2       3       4       5
    #0->L	( 0, 0)	(-1, 0)	(+2, 0)	(-1,+2)	(+2,-1)
    #L->2	( 0, 0)	(-2, 0)	(+1, 0)	(-2,-1)	(+1,+2)
    #2->R	( 0, 0)	(+1, 0)	(-2, 0)	(+1,-2)	(-2,+1)
    #R->0	( 0, 0)	(+2, 0)	(-1, 0)	(+2,+1)	(-1,-2)

    def rotate_left(self, grid: list[list[str]]) -> bool :
        if self.check(self.x, self.y, self.rotation - 1, grid):
            self.rotation -= 1
            return True

        tests: list[tuple[int,int]] = [(-1,-1)]
        if self.shape == Shape.SHAPE_L:
            if self.rotation == 0:
                tests = [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, 2)]
            if self.rotation == 1:
                tests = [(0, 0), (-1, 0), (-1, 1), (0,-2), (-1, -2)]
            if self.rotation == 2:
                tests = [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)]
            if self.rotation == 3:
                tests = [(0, 0), (+1, 0), (1, 1), (0, -2), (1, -2)]
        else:
            if self.rotation == 0:
                tests = [(0, 0), (1, 0), (2, 0), (-1, 2), (2, -1)]
            if self.rotation == 1:
                tests = [(0, 0), (2, 0), (1, 0), (-2, -1), (1, 2)]
            if self.rotation == 2:
                tests = [(0, 0), (1, 0), (-2, 0), (+1, -2), (-2, 1)]
            if self.rotation == 3:
                tests = [(0, 0), (2, 0), (-1, 0), (+2, 1), (-1, -2)]

        for test in tests:
            if self.check(self.x + test[0], self.y + test[1], self.rotation + 1, grid):
                self.x += test[0]
                self.y += test[1]
                self.rotation += 1
                return True
        return False

    def check(self, x: int, y: int, rotation: int, grid: list[list[str]]) -> bool:
        new_tetromino: list[str] = self.shape.value[rotation % len(self.shape.value)]
        for i in range(4):
            for j in range(4):
                try:
                    if new_tetromino[i][j] == 'o' and grid[x + i][y + j] != (0,0,0):
                        return False
                except IndexError:
                    continue

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
        self.rotation = 0
