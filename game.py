import pygame
from objects.board import Board
from constants import ARROWS, NUMBERS, WHITE


class Game:
    def __init__(self) -> None:
        self.active = True
        self.board = Board()

    def click(self, x: int, y: int) -> None:
        self.board.select(x, y)

    def press_key(self, key: int) -> None:
        if key in ARROWS:
            self.board.move(ARROWS[key])

        if key in NUMBERS:
            self.board.edit(NUMBERS[key])

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.fill(WHITE)
        self.board.draw(screen)
