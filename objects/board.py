import pygame
from sudoku import Sudoku
from objects.object import Object
from constants import WHITE, YELLOW, BLUE, BLACK


class Board(Object):
    def __init__(self, difficulty=0.5) -> None:
        super().__init__()
        self.original = Sudoku(3).difficulty(difficulty).board
        self.nums = [row.copy() for row in self.original]
        self.status = [[None for _ in range(9)] for _ in range(9)]
        self.selected_row, self.selected_col = -1, -1

    def selected_square(self) -> bool:
        return self.selected_row != -1 and self.selected_col != -1

    def get_x(self, col: float) -> float:
        return self.x_padd + self.unit_size * 9 + col * self.cell_size

    def get_y(self, row: float) -> float:
        return self.y_padd + self.unit_size + row * self.cell_size

    def select(self, x: int, y: int) -> None:
        if x >= self.get_x(0) and y >= self.get_y(0) and x <= self.get_x(9) and y <= self.get_y(9):
            # find the row and col
            self.selected_row = int((y - self.get_y(0)) // self.cell_size)
            self.selected_col = int((x - self.get_x(0)) // self.cell_size)

    def move(self, direction: str) -> None:
        if self.selected_square():
            if direction == "left":
                self.selected_col = max(0, self.selected_col - 1)
            elif direction == "right":
                self.selected_col = min(8, self.selected_col + 1)
            elif direction == "up":
                self.selected_row = max(0, self.selected_row - 1)
            elif direction == "down":
                self.selected_row = min(8, self.selected_row + 1)

    def edit(self, number: int) -> None:
        if self.selected_square():
            # if that number isn't on the original board
            if self.original[self.selected_row][self.selected_col] is None:
                self.nums[self.selected_row][self.selected_col] = number

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw squares and numbers
        for row in range(9):
            for col in range(9):
                if row == self.selected_row and col == self.selected_col:
                    colour = YELLOW
                elif self.original[row][col]:
                    colour = BLUE
                else:
                    colour = WHITE

                pygame.draw.rect(
                    screen,
                    colour,
                    (self.get_x(col), self.get_y(row), self.cell_size, self.cell_size),
                )

                number = self.nums[row][col]

                # if there is a number draw it on the square
                if number:
                    width, height = self.font.size(str(number))
                    font_surf = self.font.render(str(number), True, BLACK)
                    screen.blit(
                        font_surf,
                        (self.get_x(col + 0.5) - width // 2, self.get_y(row + 0.5) - height // 2),
                    )

        # draw lines
        for i in range(10):
            line_width = self.big_line_size if i % 3 == 0 else self.line_size

            # vertical lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.get_x(i), self.get_y(0)),
                (self.get_x(i), self.get_y(9)),
                line_width,
            )
            # horizontal liens
            pygame.draw.line(
                screen,
                BLACK,
                (self.get_x(0), self.get_y(i)),
                (self.get_x(9), self.get_y(i)),
                line_width,
            )
