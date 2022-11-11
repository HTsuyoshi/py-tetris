from pygame.font import Font, SysFont

from enum import Enum

class Soft_drop(Enum):
    NORMAL = 0
    INSTANT = 1

### Settings ###

TETROMINO_SHOWN: int = 5
TETROMINO_SHADOW: bool = True
FPS: int = 60
FALL_SPEED: int = FPS // 2
LOCK_DELAY: int = FPS * 10
KEY_REPEAT_INTERVAL: int = 20
KEY_REPEAT_DELAY: int = 150
SOFT_DROP: Soft_drop = Soft_drop.INSTANT

### Graphics ###
# General
WINDOW_H: int = 800
WINDOW_W: int = int(WINDOW_H * 1.25)
WINDOW_CENTER: tuple[int,int] = (WINDOW_W // 2, WINDOW_H // 2)
RATIO: int = 10
FONT: Font = SysFont('Source Code Variable', 30)

# Game
BRICK_SIZE: int = (((RATIO - 1) * WINDOW_H // RATIO) - (WINDOW_H // RATIO)) // 20
GAME_H_START: int = (WINDOW_H // RATIO) - BRICK_SIZE
GAME_H_END: int = ((RATIO - 1) * WINDOW_H // RATIO) + BRICK_SIZE
GAME_W_START: int = ((10 * WINDOW_W) // 16) - (((GAME_H_END - BRICK_SIZE) - (GAME_H_START + BRICK_SIZE)) // 4)
GAME_W_END: int = ((10 * WINDOW_W) // 16) + (((GAME_H_END - BRICK_SIZE) - (GAME_H_START + BRICK_SIZE)) // 4)
NEXT_TETROMINO_W: int = (GAME_W_END + WINDOW_W // 6) - (2 * BRICK_SIZE)
NEXT_TETROMINO_H: int = (GAME_H_START + WINDOW_H // 6) - (2 * BRICK_SIZE)
HOLD_TETROMINO_W: int = (GAME_W_START - WINDOW_W // 12) - (2 * BRICK_SIZE)
HOLD_TETROMINO_H: int = (GAME_H_START + WINDOW_H // 6) - (2 * BRICK_SIZE)
OFFSCREEN_BRICK_SIZE: int = 20
BORDER: int = 10

# Title
BUTTON_H: int = WINDOW_H // 16
BUTTON_W: int = WINDOW_W // 4
TITLE_W_START: int = (WINDOW_W // 2) - (BUTTON_W // 2)
TITLE_H_START: int = 6 * (WINDOW_H // 16)
TITLE_H_SIZE: int = 14 * (WINDOW_H // 16)
ICON_H: int = 2 * (BUTTON_H)
ICON_W: int = (11 * BUTTON_W) // 8
TITLE_ICON_W_START: int = (WINDOW_W // 2) - (ICON_W // 2)
TITLE_ICON_H_START: int = 2 * (WINDOW_H // 16)
