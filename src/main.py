import pygame

from Screen import Screen

from Options import WINDOW_H, WINDOW_W, KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL

if __name__ == '__main__':
    #pygame.display.set_icon(ICON)
    pygame.display.set_caption("Tetris")
    pygame.init()
    # Remover e colocar em opcoes no Title()
    pygame.key.set_repeat(KEY_REPEAT_DELAY, KEY_REPEAT_INTERVAL)
    Screen()
