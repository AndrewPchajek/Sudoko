import pygame

# the default width and height of the window, and the minimum width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
MIN_WIDTH = 400
MIN_HEIGHT = 320

# colours in rgb
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (200, 200, 255)
YELLOW = (255, 255, 175)

# pygame keys
NUMBERS = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_DELETE: None,
    pygame.K_BACKSPACE: None,
}
ARROWS = {
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
}
