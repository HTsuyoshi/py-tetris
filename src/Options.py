TETROMINO_SHOWN: int = 5
FPS: int = 60
FALL_SPEED: int = FPS // 5
LOCK_DELAY: int = FPS * 4
KEY_REPEAT_INTERVAL: int = 20
KEY_REPEAT_DELAY: int = 150
WINDOW_H: int = 800
WINDOW_W: int = int(WINDOW_H * 1.25)
RATIO: int = 10
BRICK_SIZE: int = (((RATIO - 1) * WINDOW_H // RATIO) - (WINDOW_H // RATIO)) // 20
GAME_H_START: int = (WINDOW_H // RATIO) - BRICK_SIZE
GAME_H_END: int = ((RATIO - 1) * WINDOW_H // RATIO) + BRICK_SIZE
GAME_W_START: int = (WINDOW_W // 2) - (((GAME_H_END - BRICK_SIZE) - (GAME_H_START + BRICK_SIZE)) // 4)
GAME_W_END: int = (WINDOW_W // 2) + (((GAME_H_END - BRICK_SIZE) - (GAME_H_START + BRICK_SIZE)) // 4)
NEXT_TETROMINO_W: int = (GAME_W_END + WINDOW_W // 6) - (2 * BRICK_SIZE)
NEXT_TETROMINO_H: int = (GAME_H_START + WINDOW_H // 6) - (2 * BRICK_SIZE)
HOLD_TETROMINO_W: int = (GAME_W_START - WINDOW_W // 6) - (2 * BRICK_SIZE)
HOLD_TETROMINO_H: int = (GAME_H_START + WINDOW_H // 6) - (2 * BRICK_SIZE)
OFFSCREEN_BRICK_SIZE: int = 20
BORDER: int = 10
