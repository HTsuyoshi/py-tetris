import pygame

from Screen import Screen

from Options import WINDOW_H, WINDOW_W

if __name__ == '__main__':
    #pygame.display.set_icon(ICON)
    pygame.display.set_caption("Tetris")
    pygame.init()
    Screen()
