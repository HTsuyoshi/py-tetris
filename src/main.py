import pygame

if __name__ == '__main__':
    pygame.init()
    #pygame.display.set_icon(ICON)
    pygame.display.set_caption("Tetris")
    from Screens.Screen import Screen
    Screen()
