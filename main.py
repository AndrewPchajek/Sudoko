import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MIN_WIDTH, MIN_HEIGHT

pygame.init()

pygame.display.set_caption("Sudoku")
pygame.display.set_icon(pygame.image.load("assets/icon.svg"))


def main() -> None:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    while True:
        for event in pygame.event.get():
            # if the user hits the x button quit the application
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.VIDEORESIZE:
                # make the size at least the minimum
                width, height = event.size
                width = max(width, MIN_WIDTH)
                height = max(height, MIN_HEIGHT)

                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        # update the screen
        pygame.display.flip()


# run the program
if __name__ == "__main__":
    main()
